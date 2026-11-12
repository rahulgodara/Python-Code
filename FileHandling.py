"""
file = open("E:\\Python\\demo.txt", "w")
file.write("Hello Python\n")
file.write("This is a file")
file.close()

file = open("E:\\Python\\demo.txt", "r")
content = file.read()
print(content)
file.close()

file = open("E:\\Python\\demo.txt", "a")
file.write("\nThis is an appended line")
file.close()
print()
file = open("E:\\Python\\demo.txt", "r")
content = file.read()
print(content)
file.close()

with open("E:\\Python\\demo.txt", "w") as file:
    file.write("Hello from Python")

with open("E:\\Python\\demo.txt", "r") as file:
    for line in file:
        print(line)
"""
print()
print()
with open("E:\\Python\\demo1.txt", "w") as file:
    with open("E:\\Python\\demo.txt", "r") as source_file:
        for line in source_file:
            file.write(line)

with open("E:\\Python\\demo1.txt", "r") as file:
    for line in file:
        print(line, end="")
print()
with open("E:\\Python\\demo.txt", "r") as file:
    content = file.read()
    print(content)
