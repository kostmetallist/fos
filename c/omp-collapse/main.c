#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

#define  N 10000

int main(int argc, char *argv[]) {

    srand(time(NULL));
    double **matrix = (double **) malloc(sizeof(double *) * N);
    for (int i = 0; i < N; ++i) {

        double *row = (double *) malloc(sizeof(double) * N);
        matrix[i] = row;
        for (int j = 0; j < N; ++j) {
            matrix[i][j] = (double) (rand()/RAND_MAX);
        }
    }

    double ts = omp_get_wtime();
    long long counter = 0;

    /*
        Collapse clause forces OpenMP to convert nested loops into 
        `n` ones where `n` is specified as a clause parameter. Such 
        construct usage is reasonable when available threads number 
        exceeds external loop iteration number.
    */
    #pragma omp parallel for collapse(2) 
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (matrix[i][j] > 0.5) { counter++; }
        }
    }

    printf("elapsed time: %lf\n", omp_get_wtime()-ts);
    return 0;
}
