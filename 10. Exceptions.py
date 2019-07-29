while True:
    try:
        number = int(input("Enter any number : "))
        print("1/{} = ".format(number) + str(1/number))
        break
    except ValueError:
        print("\nMake sure to enter a number only")
    except ZeroDivisionError:
        print("\nDon't enter zero")
    finally:
        print(":)\n\n")



'''
An exception is an unwanted or unexpected event, which occurs during the execution of a program i.e at run time, that disrupts the normal flow of the program’s instructions.

>>>>>> Error vs Exception
Error: An Error indicates serious problem that a reasonable application should not try to catch.
Exception: Exception indicates conditions that a reasonable application might try to catch.

We can handle these exceptions in Python so that our program will continue wih execution.

Here 'try' block is the block where exception might occur and 'except' block are for specific exceptions that'll execute on that exception.
'finally' block is executed always after the execution of 'try' and 'except' blocks.
We can instruct users using 'except' block or we can give the exception information etc.
'''