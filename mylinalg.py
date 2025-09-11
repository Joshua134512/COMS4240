import math
from matplotlib import pyplot as plt
import numpy

class Vector():
    
    def __init__(self, vector: list):
        self.vector = [float(element) for element in vector]

    def __getitem__(self, key) -> float:
        return self.vector[key]
    
    def __setitem__(self, key, value):
        self.vector[key] = float(value)

    def __delitem__(self, key):
        del self.vector[key]

    def __len__(self):
        return len(self.vector)
    
    def __add__(self, vector):
        if not isinstance(vector, Vector):
            raise Exception(f"Cannot add {type(vector)} to vector")
        if len(self) != len(vector):
            raise Exception("Vectors must me the same size")
        rtn = []
        for i in range(len(self)):
            rtn.append(self[i] + vector[i])
        return Vector(rtn)

    def __sub__(self, vector):
        if not isinstance(vector, Vector):
            raise Exception(f"Cannot add {type(vector)} to vector")
        if len(self) != len(vector):
            raise Exception("Vectors must me the same size")
        rtn = []
        for i in range(len(self)):
            rtn.append(self[i] - vector[i])
        return Vector(rtn)
    
    def __str__(self):
        return " ".join([str(element) for element in self.vector])
    
    def scale(self, scalar):
        return Vector([scalar * element for element in self])
    
    def swap(self, x1, x2):
        temp = self.vector[x1]
        self.vector[x1] = self.vector[x2]
        self.vector[x2] = temp

class Array():

    def __init__(self, array: list[list[int]]):
        self.array = [Vector(vector) for vector in array]

    def loc(self, x, y):
        return self.array[y][x]
    
    def swap_rows(self, y1, y2):
        temp = self.array[y2]   
        self.array[y2] = self.array[y1]
        self.array[y1] = temp

    @property
    def num_columns(self):
        return len(self.array[0])
    
    @property
    def num_rows(self):
        return len(self.array)
    
    def __str__(self):
        string = ""
        for row in self.array:
            for element in row:
                string += f"{element} "
            string += "\n"
        return string

def _get_nonzero_row(array: Array, vector: Vector, row: int, index: int):
    # Given an array and vector, and a row and position in that row. Swap with rows below it until the index in given row is nonzero
    num_rows = array.num_rows
    for i in range(row, num_rows):
        if array.loc(index, row) != 0:
            return
        else:
            array.swap_rows(row, i)
            vector.swap(row, i)
    if array.loc(index, row) != 0:
        return
    Exception("Columns are not linearly independent")

def gauss_elimination(a: Array, b: Vector):
    # Get into row echelon form
    num_rows = a.num_rows
    if len(b) != num_rows:
        raise Exception("Number of elements in b must match number of rows in a")
    if num_rows != a.num_columns:
        raise Exception("Must be a square matrix")
    for i in range(num_rows):
        if a.loc(i, i) == 0:
            _get_nonzero_row(a, b,i, i)
        for j in range(i+1, num_rows):
            if a.loc(i, j) != 0:
                factor = a.loc(i, j) / a.loc(i, i)
                a.array[j] = a.array[j]-a.array[i].scale(factor)
                b[j] = b[j]-b[i]*factor
    # Retrieve the answers here
    answers = [0]*num_rows
    for i in range(num_rows-1, -1, -1):
        if a.loc(i, i) == 0:
            raise Exception("Columns are not linearly independent")
        answer = b[i]
        for j in range(num_rows-1, i, -1):
            answer -= answers[j]*a.loc(j, i)
        answers[i] = answer / a.loc(i, i)
    return answers

if __name__ == "__main__":
    row1 = [math.pow(-0.1, 3), math.pow(-0.1, 2), -0.1, 1]
    row2 = [math.pow(-0.02, 3), math.pow(-0.02, 2), -0.02, 1]
    row3 = [math.pow(0.1, 3), math.pow(0.1, 2), 0.1, 1]
    row4 = [math.pow(0.02, 3), math.pow(0.02, 2), 0.02, 1]
    vector = Vector([math.cos(-0.1), math.cos(-0.02), math.cos(0.1), math.cos(0.02)])
    array = Array([row1, row2, row3, row4])
    a, b, c ,d = gauss_elimination(array, vector)

    x_values = numpy.linspace(0, 10, 100)
    fx = numpy.array([math.cos(x) for x in x_values])
    px = numpy.array([a * math.pow(x, 3) + b * math.pow(x, 2) + c * x + d for x in x_values])

    print(f"P(0.5) = {a*0.5**3+b*0.5**2+c*0.5+d}")
    print(f"F(0.5) = {math.cos(0.5)} ")

    plt.scatter(x_values, fx, label = "F(x)")
    plt.scatter(x_values, px, label = "P(x)")
    plt.title("Orange: P(X), Blue: F(X)")
    plt.savefig("/mnt/c/users/josh/ComS4240.png")
