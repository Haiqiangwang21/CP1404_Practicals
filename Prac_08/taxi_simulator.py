from Prac_08.car import Car
from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uite, c)hoose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    total_cost = 0

    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            display_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            km_driven = int(input("Drive how far? "))
            current_taxi.drive(km_driven)
            trip_cost = current_taxi.get_fare()
            total_cost += trip_cost
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("The total is: ${:.2f}".format(total_cost))


def display_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))

main()