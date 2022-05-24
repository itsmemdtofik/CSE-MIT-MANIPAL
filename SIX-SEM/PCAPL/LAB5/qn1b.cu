#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>

/**
*Write a program in cuda to add two vectors of length N Using
(a)N threads
*/
__global__ void vecAddKernel1b(int *A, int *B, int *C)
{
    int id = threadIdx.x;
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
    vecAddKernel1b<<<1, N>>>(d_A, d_B, d_C);
    // Copy result back to host
    cudaError_t err = cudaMemcpy(&C, d_C, size, cudaMemcpyDeviceToHost);
    if (err != cudaSuccess)
    {
        printf("CUDA error copying to Host: %s\n", cudaGetErrorString(err));
    }
    printf("1b. Vector Addition using N= %d threads within a block\n", N);
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
    printf("\n");
    // Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    return 0;
}