

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>
#include <ctype.h>

int main(int argc, char *argv[])
{

	int myRank;
	int size;
	char str[100];
	int stringSize;
	MPI_Status myStatus;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if (myRank == 0)
	{
		printf("Enter the string : \n");
		scanf("%s", str);
		stringSize = strlen(str);
		printf("Process sent string [ %s ] from process [ %d ] \n", str, myRank);
		MPI_Ssend(&stringSize, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
		MPI_Ssend(&str, stringSize, MPI_CHAR, 1, 1, MPI_COMM_WORLD);
		MPI_Recv(&str, stringSize, MPI_CHAR, 1, 1, MPI_COMM_WORLD, &myStatus);
		printf("Process received string [ %s ] from process [ %d ]\n", str, myRank);
	}
	else
	{
		
		MPI_Recv(&stringSize, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &myStatus);
		MPI_Recv(&str, stringSize, MPI_CHAR, 0, 1, MPI_COMM_WORLD, &myStatus);
		printf("Process recieved string [ %s ] from process [ %d ]\n", str, myRank);
		for (int i = 0; i < stringSize; i++)
		{
			if (islower(str[i]))
				str[i] = toupper(str[i]);
			else if (isupper(str[i]))
				str[i] = tolower(str[i]);
		}
		printf("Process sent the string [ %s ] from process [ %d ] \n", str, myRank);
		MPI_Ssend(&str, stringSize, MPI_CHAR, 0, 1, MPI_COMM_WORLD);
	}
	MPI_Finalize();
	return 0;
}
