#ifndef __QUAD_H_
#define __QUAD_H_

typedef struct Point Point;
    struct Point {
        float x;
        float y;
    };

typedef struct Quad Quad;
    struct Quad {
        Point point1;
        Point point2;
        Point point3;
        Point point4;
    };

#endif