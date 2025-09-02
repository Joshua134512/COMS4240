def factorial(x: int):
    ans = 1
    while(x > 0):
        ans *= x
        x -= 1
    return ans

def estimate_ex(x):
    e = 2.7182818284590451
    ex = None
    x0 = round(x)
    inner_parentheses = 0
    z = x - x0
    for i in range(10):
        inner_parentheses += (z**i / factorial(i))
    ex = e**x0 * inner_parentheses
    return ex

def yield_next_iter_ln(s, x):
    while True:
        s = s - 1 + x * estimate_ex(-s)
        yield s

def estimate_ln(x):
    generator = yield_next_iter_ln(x, x)
    for i in range(10):
        x = next(generator)
    return x

if __name__ == "__main__":
    inp = input("Select an option:\n1. Estimate e^x\n2. Estimate Ln(x)\n")

    match inp:
        case "1":
            print(estimate_ex(int(input("Enter x: "))))
        case "2":
            print(estimate_ln(int(input("Enter x: "))))
        case _:
            "Invalid option"