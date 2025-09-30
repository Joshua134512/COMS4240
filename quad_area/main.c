#include "quad.h"
#include "quad_perimeter.h"
#include "quad_area.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
    float input_x[4];
    float input_y[4];

    for(int i = 0; i < 4; i++) {
        printf("Enter next x coordinate");
        scanf("%f", &input_x[i]);
        printf("Enter next y coordinate");
        scanf("%f", &input_y[i]);
    }
    Quad quad;
    quad.point1.x = input_x[0];
    quad.point1.y = input_y[0];
    quad.point2.x = input_x[1];
    quad.point2.y = input_y[1];
    quad.point3.x = input_x[2];
    quad.point3.y = input_y[2];
    quad.point4.x = input_x[3];
    quad.point4.y = input_y[3];
    float perimeter = calc_quad_perimeter(quad);
    printf("Perimeter of quad is %f", perimeter);
    printf("\n");
    float area = calc_quad_area(quad);
    printf("Area of quad is %f", area);
    printf("\n");
}