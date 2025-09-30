main.exe: quad_area.o quad_perimeter.o main.o
	gcc quad_area.o quad_perimeter.o main.o -o main.exe -lm

quad_area.o: quad_area.c
	gcc -c quad_area.c

quad_perimeter.o: quad_perimeter.c
	gcc -c quad_perimeter.c

help:
	echo test