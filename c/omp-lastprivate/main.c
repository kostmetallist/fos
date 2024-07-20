#include <stdio.h>
#include <omp.h>

int main(int argc, char *argv[]) {

    long long tmp = 0;
    double ts = omp_get_wtime();
    #pragma omp parallel num_threads(4) for firstprivate(tmp) lastprivate(tmp)
    for (int j = 0; j < 100000; ++j) {
        tmp += j;
    }

    /*
        as described in documentation, `tmp` in master thread will be 
        defined with its value at the "last sequential" iteration (for j=999)
    */
    printf("time elapsed: %lf\n", omp_get_wtime()-ts);
    printf("tmp=%lld\n", tmp);
    return 0;
}
