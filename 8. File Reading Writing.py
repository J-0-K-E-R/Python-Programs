file = open('test.txt', 'w')            # This will open/create a file 'test.txt' with write mode.
file.write("First line.\n")              # Writing into the file.
file.close()                            # Closing a file object. It's necessary to close the file.

file = open('test.txt', 'a')            # This will open file 'test.txt' with append mode.
file.write("This is second line.\n")
file.close()


file = open('test.txt', 'r')            # This will open file 'test.txt' with read mode.
text = file.read()
print(text)
file.close()


'''
We can open a file using modes read, write, append and read+ (for both write and read)
Write can create a file whereas others can't.
Default argument is r.
'''