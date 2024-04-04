#include <stdio.h>
#include <math.h>
#include<complex.h>

#define NUM_POINTS 1000

double H(double omega) {
    double complex num = cpow(2.71, -2 * I * omega) + 1;
    double complex den = cpow(2.71, -1 * I * omega)/2 + 1;
    double complex h = num/den;
    return cabs(h);
}

int main() {
    double omega = 0;
    FILE *fp;

    fp = fopen("4.5.dat", "w");
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    for (int i = 0; i < NUM_POINTS; ++i) {
        omega = -3 * 3.14 + (6 * 3.14 * i) / (NUM_POINTS);
        fprintf(fp, "%f %f\n", omega, H(omega));
    }

    fclose(fp);

    return 0;
}
