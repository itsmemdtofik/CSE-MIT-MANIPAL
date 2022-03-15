#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[])
{

	int number1 = 10;
	int number2 = 4;
	int add;
	int sub;
	int mul;
	int div;
	int myRank;
	int size;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);		

		if (myRank == 0)
		{
			add = number1 + number2;
			printf("Addition is = [ %d ] : with rank [ %d ]\n", add, myRank);
		}
		else if (myRank == 1)
		{
			sub = number1 - number2;
			printf("Substraction is = [ %d ] : with rank [ %d ]\n", sub, myRank);
		}
		else if (myRank == 2)
		{   
			mul = number1 * number2;
			printf("Multiplication is = [ %d ] : with rank [ %d ]\n", mul, myRank);
		}
		else if (myRank == 3)
		{   
			div = number1 / number2;
			printf("Division is = [ %d ] : with rank [ %d ]\n", div, myRank);
		}
		else
		{
			printf("\n");
		}
	
	MPI_Finalize();
	return 0;
}