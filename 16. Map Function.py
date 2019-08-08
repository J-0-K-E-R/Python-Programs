# Map function is used to iterate a list of variable to run each through a function easily instead of using loops

numbers = [7, 54, 79, 85, 65]


def square(num):
    return num * num


output = list(map(square, numbers))
print(output)