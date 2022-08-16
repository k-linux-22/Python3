def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b
def default():
    return "Option Not Available"

switcher = {
    1: add,
    2: sub,
    3: mult,
    4: div
}

def calc(work, a, b):
    # a = int(input("Enter first number : "))
    # b = int(input("Enter second number : "))
    return switcher.get(work, default)(a, b)

if __name__ == "__main__":
    process = int(input("""Enter:
    1 for Addition
    2 for Subtraction
    3 for Multiplication
    4 for Division \n"""))
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(calc(process, a, b))
