#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("assign3.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
//Generate x and y values	
    for (int i = 0; i < 10000; i++) {
        double x = i / 100.0;
        double y = floor((x + 9.8) / 19.6);
        fprintf(file, "%.2f %.0f\n", x, y);
    }

    fclose(file);
    return 0;
}
