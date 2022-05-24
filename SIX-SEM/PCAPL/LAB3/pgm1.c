#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

int fact(int n)
{
	int fact = 1;
	for (int i = 1; i <= n; i++)
	{
		fact = fact * i;
	}
	return fact;
}

int main(int argc, char *argv[])
{

	int myRank;
	int size;
	int sendBuffer[4];
	int recvdBuffer[4];
	int rootRank = 0;
	int N;
	int calc;
	int sum = 0;

	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

	if (size != 4)
	{
		printf("This process will work with 4 process : ");
		MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
	}

	if (myRank == rootRank)
	{
		N = size;
		printf("Enter the size of an array : \n");
		scanf("%d", &N);
		printf("Enter the elements of an array : \n");
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &sendBuffer[i]);
		}
	}

	MPI_Scatter(&sendBuffer, 1, MPI_INT, &calc, 1, MPI_INT, rootRank, MPI_COMM_WORLD);
	fprintf(stdout, "I have recieved number [ %d ] from  process [ %d ] \n", calc, myRank);
	fflush(stdout);
	calc = fact(calc);
	MPI_Gather(&calc, 1, MPI_INT, &recvdBuffer, 1, MPI_INT, rootRank, MPI_COMM_WORLD);

	if (myRank == rootRank)
	{
		fprintf(stdout, "The factorial of all prcess are gathered : \n");
		N = size;
		for (int i = 0; i < N; i++)
		{
			fprintf(stdout, "%d\t", recvdBuffer[i]);
			fflush(stdout);
		}
		printf("\n");
	}
	N = size;
	for (int i = 0; i < N; i++)
	{
		sum = sum + recvdBuffer[i];
	}
	if (myRank == rootRank)
	{
		printf("The sum of all gatered data is = %d\n", sum);
	}
	MPI_Finalize();
	return 0;
}