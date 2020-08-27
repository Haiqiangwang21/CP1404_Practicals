numbers = [3, 1, 4, 1, 5, 9, 2]

# 3 is chosen
print(numbers[0])

# 2 is chosen
print(numbers[-1])

# 1 is chosen
print(numbers[3])

# 3, 1, 4, 1, 5, 9 is chosen
print(numbers[:-1])

# 1 is chosen
print(numbers[3:4])

# yes 5 is in the list numbers
if 5 in numbers:
    print("Yes, 5 is in numbers list")

# yes 7 is in the list numbers
if 7 in numbers:
    print("Yes, 7 is in numbers list")

# no '3' is not in list numbers
if "3" in numbers:
    print("Yes '3' is in numbers list")
else:
    print("No '3' is not in numbers list")

# adds 6, 5, 3, to the list 'number' forming a new list
numbers_1 = numbers + [6, 5, 3]
print(numbers_1)

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)

# 2. Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

# 3. Get all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Check if 9 is an element of numbers
if 9 in numbers:
    print("Yes '9' is in numbers list")
else:
    print("No '9' is not in numbers list")