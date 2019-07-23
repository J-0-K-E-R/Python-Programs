#   Function to perform simple mathematics operations on two numbers
def calculator(a = 1, b = 1):
    print("Sum is", a+b)
    print("Subtraction is", a-b)
    print("Multiplication is", a*b)
    print("Division is", a/b)

# Function to calculate a factorial and return it's value
def factorial(i = 1):
    if i in [0, 1]:
        return 1
    else:
        return i*factorial(i-1)

print("Enter two numbers.")
print("a = ", end = "")
a = int(input())
print("b = ", end = "")
b = int(input())
calculator(a, b)

print("Enter any number: ", end="")
x = int(input())
print("Factorial of {} is {}".format(x, factorial(x)))