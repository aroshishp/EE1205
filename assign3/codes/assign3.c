#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("assign3.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
//Generate V_in and V_out values	
    for (int i = 0; i < 10000; i++) {
        double V_in = i / 100.0;
        double V_out = floor((V_in + 9.8) / 19.6);
        fprintf(file, "%.2f %.0f\n", V_in, V_out);
    }

    fclose(file);
    return 0;
}
