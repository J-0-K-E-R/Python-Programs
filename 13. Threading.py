# A thread is a separate flow of execution. This means that your program will have two things happening at once.
# It means we can run thread in parallel.

import threading


class Threads(threading.Thread):                            # Creating a child class of class Thread
    def run(self):                                          # Run is necessary for a thread. It is the part that executes in the thread.
        for _ in range(0, 10):
            print(threading.currentThread().getName())


t1 = Threads(name="Thread1")
t2 = Threads(name="Thread2")

t1.start()                                                  # 'start' method is used to run a thread. Upon calling 'start', it'll look for 'run' method and execute it.
t2.start()