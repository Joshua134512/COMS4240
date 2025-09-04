# Factorial, uses a loop to multiply numbers until it reaches 1
def factorial(x: int):
    ans = 1
    while(x > 0):
        ans *= x
        x -= 1
    return ans

# This function estimates e^x
def estimate_ex(x):
    e = 2.7182818284590451
    ex = None
    x0 = round(x)
    inner_parentheses = 0
    z = x - x0
    for i in range(10):
        inner_parentheses += (z**i / factorial(i)) # This calculates part of the equation for newton's method
    ex = e**x0 * inner_parentheses # This puts the pieces together to get the final answer
    return ex

# Estimates ln(x) using newton's method
def estimate_ln(x):
    s = x
    for i in range(10):
        s = s - 1 + x * estimate_ex(-s)
    return s

if __name__ == "__main__":
    inp = input("Select an option:\n1. Estimate e^x\n2. Estimate Ln(x)\n")

    match inp:
        case "1":
            print(estimate_ex(int(input("Enter x: "))))
        case "2":
            print(estimate_ln(int(input("Enter x: "))))
        case _:
            print("Invalid option")