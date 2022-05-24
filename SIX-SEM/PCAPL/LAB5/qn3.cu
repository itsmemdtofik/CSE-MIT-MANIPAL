#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>

__global__ void oddEven(int *a, int n)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n)
    {
        if (i % 2 == 1 && i < n - 1)
        {
            if (a[i] >= a[i + 1])
            {
                int t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
            }
        }
    }
}
__global__ void evenOdd(int *a, int n)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n)
    {
        if (i % 2 == 0 && i < n - 1)
        {
            if (a[i] >= a[i + 1])
            {
                int t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
            }
        }
    }
}
int main()
{
    int N = 5;
    // host copies of variables A, B
    int A[N] = {2, 5, 4, 3, 1};
    printf("3. Sort using Odd Even Transposition Sorting:\n");
    printf("Initial Array A elements:\n");
    for (int k = 0; k < N; k++)
    {
        printf("%d ", A[k]);
    }
    int *d_A;
    int size = N * sizeof(int);
    cudaMalloc((void **)&d_A, size);
    cudaMemcpy(d_A, &A, size, cudaMemcpyHostToDevice);
    for (int i = 0; i < N / 2; i++)
    {
        oddEven<<<ceil(N / 2.0), 2>>>(d_A, N);
        evenOdd<<<ceil(N / 2.0), 2>>>(d_A, N);
    }
    cudaMemcpy(&A, d_A, size, cudaMemcpyDeviceToHost);
    printf("\nResultant sorted Array A:\n");
    for (int i = 0; i < N; i++)
        printf("%d ", A[i]);
    return 0;
}