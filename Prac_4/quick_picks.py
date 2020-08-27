import random

numbers_per_line = 6
max = 45
min = 1

number_of_picks = int(input("Enter your picks? "))
while number_of_picks < 0:
    print("Invalid input")
    number_of_picks = int(input("Enter your picks? "))

for i in range(number_of_picks):
    quick_pick = []
    for j in range(numbers_per_line):
        number = random.randint(min, max)
        while number in quick_pick:
            number = random.randint(min, max)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))



