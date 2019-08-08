from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ' : ' + str(self.user_id)


users = [
    User("Amanda", 15),
    User("Jack", 59),
    User("Daniel", 98),
    User("Leo", 98),
    User("Mark", 8),
    User("Goku", 61),
    User("Kidou", 77),
    User("Neil", 32),
    User("Rem", 14),
    User("Kenji", 27)
]

print("Normal print :")
for user in users:
    print(user)

print("---------")

print("Sorted by name print:")
for user in sorted(users, key=attrgetter('name')):
    print(user)

print("---------")

print("Sorted by User ID print:")
for user in sorted(users, key=attrgetter('user_id')):
    print(user)