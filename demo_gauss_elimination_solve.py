from gauss_elimination_solve import Vector, Array, gauss_elimination
import numpy
import random


print("Generating random array and vectory")
a = []
n = 3
for i in range(n):
    a.append([random.randint(1, 9) for i in range(n)])
b = [random.randint(1,9) for i in range(n)]

my_array = Array(a)
my_vector = Vector(b)

print(f"Random array: \n{my_array}")
print(f"Random vector \n{my_vector}")

print(f"My answer: {gauss_elimination(my_array, my_vector)}")
print(f"Numpy's answer: {numpy.linalg.solve(numpy.array(a), b)}")