for i in range(1,6):
	print(i)
print()

for i in range(5):
	print(i)
print()

for i in range(2,11,2):
	print(i)
print()

for i in range(1,11):
    if i==6:
        print("we break the loop here")
        break
    print(i)
print()

for i in range(1,11):
    if i==6:
        print("we missed something here")
        continue
    print(i)