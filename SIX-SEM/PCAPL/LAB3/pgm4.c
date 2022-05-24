#include<mpi.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int rank, size, N, i;
  char str[20], str1[20], B[20];
  char rcv[10], rcv1[10], end[40];

  int part;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &N);

  if (rank == 0)
  {

    fprintf(stdout, "enter the first string:\n");
    scanf("%s", str);
    fprintf(stdout, "enter the second string:\n");
    scanf("%s", str1);
    fflush(stdout);
    if (strlen(str) != strlen(str1))
      exit(0);
    part = strlen(str) / N;
  }
  MPI_Bcast(&part, 1, MPI_INT, 0, MPI_COMM_WORLD);
  MPI_Scatter(str, part, MPI_CHAR, rcv, part, MPI_CHAR, 0, MPI_COMM_WORLD);
  MPI_Scatter(str1, part, MPI_CHAR, rcv1, part, MPI_CHAR, 0, MPI_COMM_WORLD);
  int k = 0;
  for (i = 0; i < part; i++)
  {
    end[k++] = rcv[i];
    end[k++] = rcv1[i];
  }
  
  MPI_Gather(end, 2 * part, MPI_CHAR, B, 2 * part, MPI_CHAR, 0, MPI_COMM_WORLD);
  if (rank == 0)
  {
    fprintf(stdout, "the result gathered in the root %s\t\n", B);

    fflush(stdout);
  }
  MPI_Finalize();
  return 0;
}