def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def power(a,b):
    return a ** b
def modulus(a,b):
    return a % b

print("Select operation: " \
"\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Modulus")

selection = input("Enter choice (1/2/3/4/5/6): ")


a = int(input("Enter first number:"))

b = int(input("Enter second number:"))


if selection == '1':
    print("Addition is ", add(a,b))
elif selection == '2':
    print("Subtraction is ", subtract(a,b))
elif selection == '3':
    print("Multiply is ", multiply(a,b))
elif selection == '4':
    print("Divide is ", divide(a,b))
elif selection == '5':
    print("Power is ", power(a,b))
elif selection == '6':
    print("Modulus is ", modulus(a,b))
else:
    print("Invalid input")