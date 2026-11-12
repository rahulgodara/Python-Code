fruits=['Apple','Banana']
fruits.append('Orange')
print(fruits)

print()
for i in range(len(fruits)):
    print(fruits[i])

print()
for fruit in fruits:
    print(fruit)

print()
squares = [x**2 for x in range(1, 6)]
print(squares)

print()
fruits.append('Grapes')
for fruit in fruits:
    print(fruit)


numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x*2 for x in numbers]
for num in doubled_numbers:
    print(num)

print()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    if num %2 ==0:
        #print(num)
        print(num, end=",")