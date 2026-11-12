name = "Rahul"
print(name)
print(name[0])
print(len(name))

print()
print(name[0:3])
print(name[1:4])

print()
print(name.upper())
print(name.lower())
print(name.replace("Rahul", "Rohan"))
print(name.split("a"))
print(name.title())
print()
message = "Hello World"
print(message)
print(message.split("|"))
print(message.strip())
print(message.replace("World", "Python"))
print("Hello" in message)

first = "Hello"
second = "Python"
print(first + " " + second)


age = 25
print(age)
print(f"My age is {age}")
print("My age is {}".format(age))
print("My age is %d" %age)
print("My age is " + str(age))
print("My age is " + repr(age))
print("My age is",age)


text = "Python is easy "
print(text)
print(text.upper())
print(len(text))
print(len(text.strip()))
print(text.replace("easy", "powerful"))
print(text)

text = text.replace("easy", "powerful")
print(text)


data = "  Rahul|30|Pune  "
cleaned = data.strip()
print(cleaned)
parts = cleaned.split("|")
print(parts)

name = "Rahul"
print(name[0])
print(name[:3])
print(name[1:4])
print(name[::2])
print(name[::-1])


# name1 = input("Enter your name: ")
# print("Your name is:", name1)

# age = input("Enter your age: ")
# print(type(age))


name = "Rahul"
print(name[::-1])
print("Hello\nWorld")
user_name = input("Enter name: ")
print("Hi " + user_name)


test = "My name is Rahul"
print(test.split(" "))