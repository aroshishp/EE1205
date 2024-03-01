#include <stdio.h>
#include <math.h>

#define N 15 // Change this to match the range of n values you need

double x_n(double r, int n) {
    return pow(r, n) * (n >= 0);
}

double y_n(double r, int n) {
    return (1 - pow(r, n+1)) / (1 - r) * (n >= 0);
}

int main() {
    double r = 1.0 / 3.0;
    int n_values[N] = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; // Adjust the values of n as needed
    double x[N];
    double y[N];
    int i;

    // Calculate x_n and y_n values
    for (i = 0; i < N; i++) {
        x[i] = x_n(r, n_values[i]);
        y[i] = y_n(r, n_values[i]);
    }

    // Save the data to a .dat file
    FILE *fp = fopen("assign8.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write x_n and y_n values to the file
    for (i = 0; i < N; i++) {
        fprintf(fp, "%d %lf %lf\n", n_values[i], x[i], y[i]);
    }

    fclose(fp);
    return 0;
}