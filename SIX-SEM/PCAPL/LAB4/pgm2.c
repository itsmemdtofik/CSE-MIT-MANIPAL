#include<stdio.h>
#include "mpi.h"

float fun(float x)
{
    return 4/(1+x*x);
}

 

int main(int argc,char *argv[])
{
    int rank,size;
    float interval,mid,height,sum,area;
    

    int error_code,len_error_string,error_class;

    char *error_string;

    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);


    if(error_code!=MPI_SUCCESS)
    {
        MPI_Error_class(error_code,&error_class);
        MPI_Error_string(error_class,error_string,&len_error_string);
        printf("%s\n",error_string);
    }

    interval=1/(float)size;
    mid=(rank*interval)+interval/2;
    height=fun(mid);
    area=height*interval;


    MPI_Reduce(&area,&sum,1,MPI_FLOAT,MPI_SUM,0,MPI_COMM_WORLD);


    if(rank==0)
    {
        fprintf(stdout,"process %d has value %f\n",rank,sum);
        fflush(stdout);
    }


    MPI_Finalize();
    return 0;
}