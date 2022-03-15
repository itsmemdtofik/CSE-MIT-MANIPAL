/*mpirun --use-hwthread-cpus -np 4*/
#include<stdio.h>
#include<stdlib.h>
#include"mpi.h"
#include<math.h>

int main(int argc, char* argv[]){
	int myRank;
	int size;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    printf("What is my Rank = %d and size is = %d", myRank, size);
    printf("\n\n");
    printf("The power of rank [ %d ] is = [ %d ]", myRank, (int)pow(2, myRank));
    printf("\n\n");
    MPI_Finalize();
	return 0;
}
