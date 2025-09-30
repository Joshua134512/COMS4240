OBJECTS = main.o fraction_add.o fraction_reduce.o get_prime_factors.o

.PHONY: clean

output.txt: main.exe
    ./main.exe > output.txt

main.exe: $(OBJECTS)
    gcc $(OBJECTS) -o main.exe

%.o: %.c 
    gcc -c $<

clean:
    rm -f $(OBJECTS) main.exe output.txt

help:
    echo hi