

/*A. Write an OpenCL kernel code that replaces the principal diagonal elements
with zero. Elements above the principal diagonal by their factorial and elements
below the principal diagonal by their sum of digits.*/

#include <CL/cl.h>

__kernel void operate(__global int *A, int count) {
  int i = get_global_id(0);
  int j = get_global_id(1);
  if (i == j) {
    // Primary diagonal
    A[i * count + j] = 0;
  } else if (i < j) {
    // Above diagonal
    int fact = 1;
    for (int k = 2; k <= A[i * count + j]; ++k)
      fact *= k;
    A[i * count + j] = fact;
  } else {
    // Below diagonal
    int z = A[i * count + j];
    int s = 0;
    while (z > 0) {
      s += (z % 10);
      z /= 10;
    }
    A[i * count + j] = s;
  }
}

/*A. Write a kernel that takes a string S and an integer array Count consisting
of elements equivalent to string length of S. It should produce the resultant
string RS which repeats every character of S, n times (where n is the integer
value in Count which is having the same index as of the character taken in S) as
shown below. Eg : Input String S Input array Count Output String RS : string
:121342
: sttriiinnnngg*/

__kernel void multiply(__global char *S, __global int *count,
                       __global char *RS) {
  size_t id = get_global_id(0);
  int si = 0, i;
  for (i = 0; i < id; ++i) {
    si += count[i];
  }
  for (i = 0; i < count[id]; ++i) {
    RS[si++] = S[id];
  }
}

/*B. Write an OpenCL kernel code which repeats each element of matrix total
element number of times and stores the result in another matrix. Sample Input (m
* n):
0
1
1
2
Sample Output (m * n * m * n):
0
0
0
0
1
1
1
1
1
1
1
1
2
2
2
2*/
__kernel void operate(__global int *A, int count, __global int *B) {
  int i = get_global_id(0);
  int j = get_global_id(1);
  int x = A[i * count + j];
  int ind = i * count + j;
  int k;
  for (k = 0; k < count * count; ++k) {
    B[ind * count * count + k] = x;
  }
}

/*Write a Parallel OpenCL Kernel code to Replace 1st row of this matrix by
Elements^(N), 2nd row elements by Elements^(N-1) and N-1 row elements by square
of each element Keeping Nth row as it is.*/

__kernel void operate(__global int *A, int count) {
  int i = get_global_id(0);
  int j = get_global_id(1);
  int k;
  int x = A[i * count + j];
  int p = x;
  for (k = 1; k < count - i; ++k) {
    p *= x;
  }
  A[i * count + j] = p;
}

/*Write an OpenCL kernel code which converts input matrix A into output matrix B
as follows: consider elements of matrix A into 4 equal parts. First part
elements should be incremented by 1, Second part elements should be incremented
by 2, Third part elements should be incremented by 3 and last part elements
should be incremented by 4. Write the kernel code which does this in parallel
for all the elements. Example, N=4*/

__kernel void operate(__global int *A, __global int *B, int count) {
  int i = get_global_id(0);
  int j = get_global_id(1);
  // 'd' is the increment value
  int d = 1 + (i >= count / 2) * 2 + (j >= count / 2);
  B[i * count + j] = A[i * count + j] + d;
}

/*Write OpenCL kernel code to calculate the value of Π.*/

__kernel void advance(__global float *output, const unsigned int count) {
  int n_rects = get_global_id(0);
  float rect_width = 1.0 / n_rects;
  float rect_left = 0.0;
  float rect_height_squared;
  float rect_height;
  float agg_area = 0.0;
  float pi;
  int i;
  if (n_rects < count) {
    for (i = 0; i < n_rects; i++) {
      rect_left += rect_width;
      rect_height_squared = 1 - rect_left * rect_left;
      if (rect_height_squared < 0.00001) {
        rect_height_squared = 0;
      }
      rect_height = sqrt(rect_height_squared);
      agg_area += rect_width * rect_height;
    }
    pi = 4 * agg_area;
    output[n_rects] = pi;
  }
}

/*A. Write an OpenCL Kernel code to perform odd-even transposition sorting in
parallel. What is grid?*/

__kernel void even(__global int *a) {
  int idx = get_global_id(0);
  int size = get_global_size(0);
  int temp;
  if ((idx % 2 == 0) && ((idx + 1) < size)) {
    if (a[idx] > a[idx + 1]) {
      temp = a[idx];
      a[idx] = a[idx + 1];
      a[idx + 1] = temp;
    }
  }
}

__kernel void odd(__global int *a) {
  int idx = get_global_id(0);
  int size = get_global_size(0);
  int temp;
  if ((idx % 2 != 0) && ((idx + 1) < size)) {
    if (a[idx] > a[idx + 1]) {
      temp = a[idx];
      a[idx] = a[idx + 1];
      a[idx + 1] = temp;
    }
  }
}

/*Write an OpenCL Kernel code to perform merge sort in parallel.*/
void __kernel CompareExchange(__global int *A, int pass, __global int *t) {
  int idx = get_global_id(0);
  int size = get_global_size(0);
  int i = idx * 2 * pass;
  int j = idx * 2 * pass + pass;
  int flag = 0, flag2 = pass;
  for (int k = 0; k <= pass; k += 1) {
    int temp2 = A[i + k];
    flag = 0;
    for (int z = 0; z < pass; z += 1) {
      int temp3 = A[j + z];
      if (A[i + k] >= A[j + z]) {
        int temp = A[i + k];
        A[i + k] = A[j + z];
        A[j + z] = temp;
        flag++;
        k++;
      }
      if (A[i + k] < A[j + z]) {
        flag++;
        k++;
      }
    }
    while (flag > 0) {
      k--;
      flag--;
    }
  }
}

