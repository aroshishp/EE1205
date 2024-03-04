#include <stdio.h>
#include <math.h>
#include <complex.h>

#define SIZE 1000

// Transfer function
double complex G(double w) {
    double complex s = w * I;
    return 3 * cexp(-4 * s) / (12 * s + 1);
}

int main() {
    FILE *fp;
    fp = fopen("assign9.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double w;
    for (int i = 0; i < SIZE; i++) {
        w = -2 + (4.0 / SIZE) * i;
        double complex Gjw = G(w);
        fprintf(fp, "%f %f\n", creal(Gjw), cimag(Gjw));
    }

    fclose(fp);
    return 0;
}
