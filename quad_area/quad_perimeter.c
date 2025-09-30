#include "quad.h"
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

float calc_quad_perimeter(Quad quad) {
    float length(Point, Point);
    float perimeter = 0;
    perimeter += length(quad.point1, quad.point2);
    perimeter += length(quad.point2, quad.point3);
    perimeter += length(quad.point3, quad.point4);
    perimeter += length(quad.point4, quad.point1);
    return perimeter;
}

float length(Point point1, Point point2) {
    return sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2));
}
