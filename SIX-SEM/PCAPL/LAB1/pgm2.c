#include<stdio.h>
#include<mpi.h>

int main(int argc, char* argv[]){
	int myRank;
	int size;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if(myRank % 2 == 0){
		printf("Hello : with even rank [ %d ]\n", myRank);
	}else{
		printf("World : with odd rank [ %d ]\n", myRank);
	}

    MPI_Finalize();
    return 0;
}