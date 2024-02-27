#include <stdio.h>
#include <math.h>
#include<complex.h>

#define NUM_POINTS 10000
#define PI 3.1415

double complex Z(double R1, double R2, double L1, double C1, double w) {
    return R2 + I*w*L1 + (R1)/(1+I*w*R1*C1);
}

int main() {
    FILE *fp;
    fp = fopen("assign6.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double R1 = 20.0;
    double R2 = 4.0;
    double C1 = 0.001/PI;
    double L1 = 0.02/PI;
    double w;
    double complex Z_out;

    for (int i = 0; i < NUM_POINTS; i++) {
        w = 4000.0 * i / (NUM_POINTS - 1);
        Z_out = Z(R1, R2, L1, C1, w);
        fprintf(fp, "%f %f\n", creal(Z_out), cimag(Z_out));
    }

    fclose(fp);
    return 0;
}
