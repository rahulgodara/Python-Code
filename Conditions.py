a = 15
print(a/2)
print(a//2)
print(a%2)

age = input("Enter your age:")
print(type(age))

age = int(input("Enter your age:"))
print("Your age is :", age)

if age%2==0:
    print("even")
else:
    print("odd")


name = input("Enter you name :")
print ("your name is :",name)

marks=int(input("Marks:"))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
else:
    print("c")


license = 'Yes'
if age>=18:
    if license=='Yes':
        print(name,"you can drive")
    else:
        print(name,"you cannot drive")
else:
    print(name,"you cannot drive")