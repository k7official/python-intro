from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)


users = [
    User('Musa', 38),
    User('Hope', 12),
    User('Sifi', 78),
    User('Captain', 33),
    User('Brian', 6),
    User('Pam', 22)
]

for user in users:
    print(user)

print('-------')
for user in sorted(users, key = attrgetter('name')):
    print(user)

print('-------')
for user in sorted(users, key = attrgetter('user_id')):
    print(user)
