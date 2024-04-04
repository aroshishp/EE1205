#include <stdio.h>
#include<math.h>

#define NH 14
#define NX 6

int main() {
    double fn[NH] = {0};
    double hn1[NH + 2] = {0};
    double hn2[NH + 2] = {0};
    double h[NH + 2] = {0};
    double x[NX] = {1.0, 2.0, 3.0, 4.0, 2.0, 1.0};
    double y[NH + NX - 1] = {0};

    // Pad hn1 with two zeros at the end
    for (int i = 0; i < NH; ++i) {
        hn1[i] = pow(-1.0 / 2, i);
    }

    // Pad hn2 with two zeros at the beginning
    for (int i = 0; i < NH; ++i) {
        hn2[i + 2] = hn1[i];
    }

    // Net impulse response
    for (int i = 0; i < NH + 2; ++i) {
        h[i] = hn1[i] + hn2[i];
    }

    // Convolution
    for (int n = 0; n < NH + NX - 1; ++n) {
        for (int k = 0; k < NH; ++k) {
            if (n - k >= 0 && n - k <= NX) {
                y[n] += x[n - k] * h[k];
            }
        }
    }

    FILE *fp;
    fp = fopen("5.6.dat", "w");
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    for (int i = 0; i < NH + NX - 1; ++i) {
        fprintf(fp, "%d %f\n", i, y[i]);
    }
    fclose(fp);

    return 0;
}
