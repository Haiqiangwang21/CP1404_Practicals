from Prac_08.unreliable_car import UnreliableCar


def main():
    reliable = UnreliableCar("reliable", 100, 90)
    unreliable = UnreliableCar("unreliable", 100, 9)

    for i in range(1, 3):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(reliable.name, reliable.drive(i)))
        print("{:12} drove {:2}km".format(unreliable.name, unreliable.drive(i)))

    print(reliable)
    print(unreliable)


main()
