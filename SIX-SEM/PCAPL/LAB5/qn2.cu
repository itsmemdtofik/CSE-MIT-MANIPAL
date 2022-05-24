#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>

__global__ void parallelSort(int *a, int *b, int N)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int pos = 0;
    int data = a[i];
    if (i < N)
    {
        for (int j = 0; j < N; j++)
            if (a[j] < data || (a[j] == data && j < i))
                pos++;
            b[pos] = data;
        }
    }
    int main()
    {
    // host copies of variables A, B
        int N = 5;
        int A[N] = {2, 5, 4, 3, 1};
        int B[N];
    // device copies of variables A, B
        int *d_A, *d_B;
    // Allocate space for device copies of A, B
        int size = N * sizeof(int);
        cudaMalloc((void **)&d_A, size);
        cudaMalloc((void **)&d_B, size);
    // Copy inputs to device
        cudaMemcpy(d_A, &A, size, cudaMemcpyHostToDevice);
    // Launch add() kernel on GPU
        parallelSort<<<ceil(N / 2.0), 2>>>(d_A, d_B, N);
    // Copy result back to host
        cudaError err = cudaMemcpy(&B, d_B, size, cudaMemcpyDeviceToHost);
        if (err != cudaSuccess)
        {
            printf("CUDA error copying to Host: %s\n", cudaGetErrorString(err));
        }
        printf("2. Parallel Selection Sort\n");
        printf("Initial array A elements:\n");
        for (int k = 0; k < N; k++)
        {
            printf("%d ", A[k]);
        }
        printf("\nResultant sorted array B elements:\n");
        for (int k = 0; k < N; k++)
        {
            printf("%d ", B[k]);
        }
    // Cleanup
        cudaFree(d_A);
        cudaFree(d_B);
        return 0;
    }