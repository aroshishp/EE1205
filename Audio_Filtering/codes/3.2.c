#include <stdio.h>

int main() {
    double x[] = {1.0, 2.0, 3.0, 4.0, 2.0, 1.0};
    int k = 20;
    double y[20] = {0};

    // Initial Values
    y[0] = x[0];
    y[1] = x[1] - y[0] / 2;

    // Recursive Relation
    for (int n = 2; n < k - 1; ++n) {
        if (n < 6) {
            y[n] = -0.5 * y[n - 1] + x[n] + x[n - 2];
        } else if (n > 5 && n < 8) {
            y[n] = -0.5 * y[n - 1] + x[n - 2];
        } else {
            y[n] = -0.5 * y[n - 1];
        }
    }

    FILE *fp;
    fp = fopen("3.2.dat", "w");
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    for (int i = 0; i < k; ++i) {
        fprintf(fp, "%d %f\n", i, y[i]);
    }
    fclose(fp);

    return 0;
}
