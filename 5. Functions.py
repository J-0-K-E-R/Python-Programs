def add_numbers(*args):                         # *<argument_name> is used for flexible number of arguments i.e. we can send as many arguments as we want to but we don't really know how many. All will be stored in args in this case.
    sum = 0
    for i in args:
        sum = sum + i
    prints(n='is', m='Sum', o=str(sum))


def prints(m='1st argument', n='2nd argument', o='3rd argument'):
    print(m, n, o)


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


prints();

add_numbers(1, 56)
add_numbers(1, 56, 16, 168, 165)
add_numbers(1, 56, 16, 168, 165, 84, 984, 981, 841, 9841)

some_numbers = [18, 965, 19, 8451, 52, 11, 34, 9897, 1321, 59, 75, 41, 5, 4, 79, 445, 13]
add_numbers(*some_numbers)                  # This is called unpacking of arguments. This will send all the values from some_numbers as seperate arguments.

prints("Enter", "two", "numbers.")
print("a = ", end = "")
a = int(input())
print("b = ", end = "")
b = int(input())
calculator(a, b)

prints(o='number: ', m='Enter', n='any')                 # Passing arguments from different positions
x = int(input())
print("Factorial of {} is {}".format(x, factorial(x)))