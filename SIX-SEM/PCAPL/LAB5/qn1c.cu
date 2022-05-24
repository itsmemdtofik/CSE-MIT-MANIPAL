#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>

/*Implement a CUDA program to add two vectors of Length N by keeping
the number of threads per block as 256(constant) and vary the
the number of blocks*/

__global__ void vecAddKernel(int *A, int *B, int *C, int N)
{
    int id = blockIdx.x * blockDim.x + threadIdx.x;
    if (id < N)
        C[id] = A[id] + B[id];
}
int main()
{
    // host copies of variables A, B & C
    int N = 5;
    int A[N] = {1, 2, 3, 4, 5};
    int B[N] = {6, 7, 8, 9, 10};
    int C[N] = {0, 0, 0, 0, 0};
    // device copies of variables A, B & C
    int *d_A, *d_B, *d_C;
    // Allocate space for device copies of A, B, C
    int size = N * sizeof(int);
    cudaMalloc((void **)&d_A, size);
    cudaMalloc((void **)&d_B, size);
    cudaMalloc((void **)&d_C, size);
    // Copy inputs to device
    cudaMemcpy(d_A, &A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, &B, size, cudaMemcpyHostToDevice);
    // Launch add() kernel on GPU
    vecAddKernel<<<ceil(N / 256.0), 256>>>(d_A, d_B, d_C, N);
    // Copy result back to host
    cudaError err = cudaMemcpy(&C, d_C, size, cudaMemcpyDeviceToHost);
    if (err != cudaSuccess)
    {
        printf("CUDA error copying to Host: %s\n", cudaGetErrorString(err));
    }
    printf("1c. Vector Addition using 256 threads per block and vary the number of blocks\n");
    printf("Elements of Array A are: ");
    for(int k=0;k<N;k++){
        printf("%d ", A[k]);
    }
    printf("\n");
    printf("Elements of Array B are: ");
    for(int k=0;k<N;k++){
        printf("%d ", B[k]);
    }
    printf("\n");
    printf("Resultant Array C is:");
    for(int k=0;k<N;k++){
        printf("%d ", C[k]);
    }
    printf("\n");
    // Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    return 0;
}