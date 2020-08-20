
def main():
    # prompt for user input and print the grade of score
    score = float(input("Enter score: "))
    print(check_score(score))


def check_score(score):
    # check user input
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")
    score = float(input("Enter score: "))


main()