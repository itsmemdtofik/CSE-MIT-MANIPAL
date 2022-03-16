#include<stdio.h>
#include<stdlib.h>
#include<mpi.h>

int main(int argc, char* argv[]){

	int number;
	int size;
	int myRank;
	MPI_Status myStatus;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
    
	if(myRank == 0){
		printf("Enter the number : \n");
		scanf("%d", &number);
		MPI_Send(&number, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
		MPI_Recv(&number , 1, MPI_INT, 3, 1, MPI_COMM_WORLD, &myStatus);
		fprintf(stdout, "Process recieved number [ %d ] in process [ %d ] from process [ %d ]\n", number, myRank, (size-1));
		fflush(stdout);
	}else if(myRank == 1){
		MPI_Recv(&number, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &myStatus);
		fprintf(stdout, "Process recieved number [ %d ] in process [ %d ] from process [ %d ]\n", number, myRank, (myRank-1));
		fflush(stdout);
		number = number + 1;

		MPI_Send(&number, 1, MPI_INT, 2, 1, MPI_COMM_WORLD);

	}else if(myRank == 2){
		MPI_Recv(&number, 1, MPI_INT, 1, 1, MPI_COMM_WORLD, &myStatus);
		fprintf(stdout, "Process recieved number [ %d ] in process [ %d ] from process [ %d ]\n", number, myRank, (myRank-1));
		fflush(stdout);
		number = number + 1;

		MPI_Send(&number, 1, MPI_INT, 3, 1, MPI_COMM_WORLD);

	}else if(myRank == 3){
		MPI_Recv(&number, 1, MPI_INT, 2, 1, MPI_COMM_WORLD, &myStatus);
		fprintf(stdout, "Process recieved number [ %d ] in process [ %d ] from process [ %d ]\n", number, myRank, (myRank-1));
		fflush(stdout);
		number = number + 1;
		MPI_Send(&number, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
	}else{
		printf("\n\n");
	}

	MPI_Finalize();
	return 0;
}