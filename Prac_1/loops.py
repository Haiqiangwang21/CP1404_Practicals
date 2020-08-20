'''
Loops presented in different scenarios

Haiqiang Wang
'''


for i in range(1, 21, 2):
    print(i, end=" ")
print()

# A) count in 10s from 0 to 100
for i in range(0, 110, 10):
    print(i, end=" ")
print()

# B) count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# C) input integer and print same amount of stars
num = int(input("Enter Number of stars: "))
for n in range(1, num + 1):
    print("*", end=" ")

# D) print n lines of increasing stars
x = int(input("Enter Number of rows: "))
for n in range(1, x + 1):
    for i in range(1, n + 1):
        print("*", end=" ")
    print()
