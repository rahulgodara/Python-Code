# try:
#     x = int("abc")
# except:
#     print("Something went wrong.")

# try:
#     value = int(input("Enter a number:"))
#     print("You entered:", value)
#     print(f"You entered: {value}")
#     print("You entered: "+ str(value))
# except ValueError:
#     print("Please enter a valid number")


# try:
#     with open("file.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# try:
#     num = int(input("Enter number: "))
#     print(10/num)
# except ValueError:
#     print("Enter only digits")
# except ZeroDivisionError as e:
#     print("Number cannot be zero", e)
#     print(e)


try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("Please enter a valid number")
