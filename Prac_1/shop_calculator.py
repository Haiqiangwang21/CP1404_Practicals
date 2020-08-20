
'''
prompting for items brought storing it in a list and summing up the total and
apply discount if price is over 100

Haiqiang Wang
'''


total = []
items = int(input("Enter item amount: "))
while items <= 0:
    print("Invalid numbers of items")
    items = int(input("Enter item amount: "))

for i in range(items):
    price = float(input("Enter Price: "))
    total.append(price)
    sum(total)

if sum(total) < 100:
    print("Total price for", items, "items is ${:.2f}".format(sum(total)))

elif sum(total) > 100:
    total = sum(total) * 0.9
    print("Total price for", items,"items is ${:.2f}".format(total))

