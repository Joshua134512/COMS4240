from myfuncs import estimate_ln, estimate_ex
import numpy as np
import random

random_number = random.random()
print(f"Random Number {random_number}")

print(f"My value for e^x is {estimate_ex(random_number)}")
print(f"Numpy's value for e^x is : {np.exp(random_number)}")

print(f"My value for ln(x) is {estimate_ln(random_number)}")
print(f"Numpy's value for ln(x) is : {np.log(random_number)}")