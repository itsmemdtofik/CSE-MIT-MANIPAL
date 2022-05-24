#include<stdio.h>
#include "mpi.h"
int main(int argc,char *argv[])
{
	int rank,size,final;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);

	int a[4][4];
	int c[4];
	if(rank==0)
	{
		fprintf(stdout,"Enter the elements of the matrix : \n");
		fflush(stdout);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		}
	}

	MPI_Scatter(a,4,MPI_INT,c,4,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Scan(c,&final,4,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
	MPI_Gather(&final,4,MPI_INT,a,4,MPI_INT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		fprintf(stdout,"The elements of the modified matrix is : \n");
		fflush(stdout);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				printf("%d\t",a[i][j]);
			printf("\n");
		}
	}
	MPI_Finalize();
	return 0;
}