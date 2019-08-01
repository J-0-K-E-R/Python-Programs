class Counter:                                              # Creating a class Counter
    counter = 0

    def __init__(self, x):                                  # Class initializer, this is called when a new instance of class is created.
        print("Counter {} initialized.".format(x))

    def incr(self):
        self.counter += 1
        print("Counter increased.", end="\n\n")

    def decr(self):
        self.counter -= 1
        print("Counter decreased.", end="\n\n")

    def check_counter(self):
        print("Counter value is", self.counter, end="\n\n")


c1 = Counter(1)                                              # Creating two objects named c1 and c2 from class Counter
c2 = Counter(2)

for i in range(0, 10):
    c1.incr()


for i in range(0, 20):
    c2.incr()

c1.check_counter()

c2.check_counter()

for i in range(0, 6):
    c1.decr()

for i in range(0, 11):
    c2.decr()

c1.check_counter()

c2.check_counter()