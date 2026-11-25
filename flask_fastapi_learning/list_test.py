def greet(name, greeting="Hello"):      # default arg
    return f"{greeting}, {name}!"

print(greet("Rahul"))
print(greet(greeting="Hi", name="A"))   # keyword args
print(greet("Rahul", "Hi"))

nums = [1,3,6,4]
print(nums)
nums.append(2)
print(nums)
nums.insert(1, 15)         # insert at index
print(nums)
nums.extend([50, 60])      # add many
print(nums)
nums.remove(3)            # remove first matching value
print(nums)
last = nums.pop()          # remove & return last (pop(0) for first)
print(nums)
print(last)
nums.sort(reverse=True)    # in-place sort
print(nums)
sorted_copy = sorted(nums) # returns new list
print(sorted_copy)
print(nums[-1])
print(nums[0])
nums.sort()
print(nums[-1])
print(nums[0])
print("len-",len(nums))
print(15 in nums)
print(nums.index(6))
print(nums.count(10))