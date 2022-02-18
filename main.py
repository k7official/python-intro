
# name = input("What is your name? ")
# print("Your name is ", name)

# assign multiple variables
player1, player2, player3 = 'ronaldo', "kaka", "messi"
print(player1)
print(player2)
print(player3)


def addFunc(a, y, z):
    result = a + y + z
    multiply = a * y * z
    difference = a - y - z
    return result, multiply, difference


print(type(addFunc(5, 6, 7)))
print(addFunc(6, 9, 0))
print(addFunc(10, 20, 30))

# Lambda anonymous


def func(j):
    return lambda v, y: v + j + y


double = func(3)
print(double(2, 9))

fruits = ["apple", "orange", "banana"]
new_fruits = ("watermelon", "leech")
print(fruits)
fruits.extend(new_fruits)
print(fruits)
fruits.append("lemon")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop(2)
print(fruits)
fruits.pop()  # deletes the last item by default
print(fruits)
# del fruits
fruits.clear()
print(fruits)
letters = ("a", "b", "c", "d")
print(letters[:2])

names = {"James", "Luka", "Mount"}
print(names)
for i in names:
    print(i)
print("Lukas" in names)
person = {
    "name": "Muller",
    "age": 30,
    "country": "Germany"
}
print(person)
print(type(person))
print(len(person))

# x = person["name"]
# x = person.items()
# x = person.values()
x = person.get("name")
print(x)

k = 1
while k < 7:
    k += 1
    if k == 3:
        continue
    print(k)
else:
    print("x is no longer less than 7!")

for x in range(3, 15, 2):
    print(x)
else:
    print("Completed")  # cannot execute else statement if break statement is used in loop
