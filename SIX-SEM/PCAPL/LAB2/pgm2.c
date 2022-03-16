#include "mpi.h"
#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(int argc,char *argv[])
{
	int myRank;
	int size;
	int number;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(myRank==0)
	{
		printf("Enter the number : \n");
		scanf("%d",&number);
		for(int i=1;i<size;i++)
		{
			MPI_Send(&number,1,MPI_INT,i,1,MPI_COMM_WORLD);
		}
	}
	else

	{
		MPI_Recv(&number,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
		fprintf(stdout,"process have recieved mumber[ %d ] from process [ %d ] \n",number, myRank);
		fflush(stdout);
	}
	MPI_Finalize();
	return 0;

}