file = open("main.txt", "r")
# print(file.read(20))

print(file.readline())
print(file.readline())
print(file.readline())
for x in file:
    print(x)
file.close()

# writing to files

file = open("main.txt", "a")
file.write("Writing new content to this file")
file.close()

file = open("main.txt", "w")
file.write("Another content to a file")
file.close()

# file = open("demo.txt", "x")
# file = open("any.txt", "w")

# import os
# os.remove("any.txt")


def beef():
    print("Functions are cool")


beef()
