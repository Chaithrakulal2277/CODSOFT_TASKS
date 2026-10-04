num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

op = input("Enter operation: ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")
        result = None
else:
    print("Invalid operation.")
    result = None

if result is not None:
    print("Result =", result)