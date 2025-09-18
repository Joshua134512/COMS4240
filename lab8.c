#include <stdio.h>
#include <math.h>

int main() {
    int factorial(int);
    double ex(double, int);

    int factorial_input;
    printf("Please enter a value to calcualte the factorial\n");
    scanf("%i", &factorial_input);
    int factorial_answer = factorial(factorial_input);
    printf("%i! = %i\n", factorial_input, factorial_answer);

    double ex_input;
    int array_size;
    printf("Enter the number of values to calculate e^x\n");
    scanf("%i", &array_size);
    double ex_inputs[array_size];
    double ex_answers[array_size];
    for(int i = 0; i < array_size; i++){
        printf("Enter the next value to calculate\n");
        scanf("%lf", &ex_inputs[i]);
        ex_answers[i] = ex(ex_inputs[i], 10);
    }
    FILE* outfile = fopen("out.data", "w");
    for(int i = 0; i < array_size; i++){
        printf("e^%lf = %lf\n", ex_inputs[i], ex_answers[i]);
        fprintf(outfile, "e^%lf = %lf\n", ex_inputs[i], ex_answers[i]);
    }

}

int factorial(int input) {
    if(input < 0) {
        printf("Recieved negative value for factorial, returning 0");
        return 0;
    }
    if(input == 1 || input == 0) {
        return 1;
    }
    return input * factorial(input - 1);
}

double ex(double input, int accuracy) {

    double e = 2.7182818284590451;
    double x0 = round(input);
    double z = input - x0;
    double loop_sum = 0;
    for(int i = 0; i < accuracy; i++) {
        loop_sum += pow(z, i)/factorial(i);
    }
    return pow(e, x0) * loop_sum;
}