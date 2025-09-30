#include "quad.h"
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

float calc_quad_area(Quad quad) {
    float calc_triangle(Point, Point, Point);
    float area = 0.0;
    area += calc_triangle(quad.point1, quad.point2, quad.point3);
    area += calc_triangle(quad.point3, quad.point4, quad.point1);
    return area;
}

float calc_triangle(Point point1, Point point2, Point point3) {
    float area = 0.0;
    float v1x = point2.x-point1.x;
    float v1y = point2.y-point1.y;
    float v2x = point3.x-point1.x;
    float v2y = point3.y-point1.y;
    area = v1x*v2y-v2x*v1y;
    area = area / 2;
    return fabs(area);
}