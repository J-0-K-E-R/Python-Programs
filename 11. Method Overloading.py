# Several ways to call a method (method overloading)
# We can use method overloading inside a class too.


def n_sum(x, y, z=0):                         # As we've set the value of z to 0, this allows us to call n_sum with two parameters only.
    return x + y + z                          # This is Method Overloading in Python. I've also used some Method Overloading in '05. Functions' practice file.


i = n_sum(1, 2)

print("Sum is", i)

j = n_sum(1, 2, 3)

print("Sum is", j)