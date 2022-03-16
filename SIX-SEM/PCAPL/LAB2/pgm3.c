#include<stdio.h>
#include<mpi.h>

int main(int argc, char* argv[]){

	int myRank;
	int size;
	int number;
	int arr[100];
	int sqr;
	int cube;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status myStatus;

	if(myRank == 0){

		printf("Enter the elements: \n");
		for(int i = 0; i < size; i++){
			scanf("%d", &arr[i]);
		}

		for(int i = 1; i < size; i++){
			MPI_Buffer_attach(arr, size);
			MPI_Bsend(&arr[i], 1, MPI_INT, i, 1, MPI_COMM_WORLD);
		}
	}else if(myRank % 2 == 0){
		MPI_Recv(&number, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &myStatus);
		sqr = number * number;
		fprintf(stdout, "I have recieved number [ %d ] from process [ %d ] with square root of number [ %d ]\n", sqr, myRank, number);
		fflush(stdout);
	}else{
		MPI_Recv(&number, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &myStatus);
		cube = number * number * number;
		fprintf(stdout, "I have recieved number [ %d ] from process [ %d ] with square root of number [ %d ]\n", cube, myRank, number);
		fflush(stdout);
	}
	MPI_Buffer_detach(&arr, &size);
	MPI_Finalize();
	return 0;

}