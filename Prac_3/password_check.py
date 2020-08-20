
PASSWORD_LENGTH = 5


def main():

    password = get_password(PASSWORD_LENGTH)
    print_asterisks(password)


def get_password(password_length):
    # Get user to input a password
    password = input("Enter a password with 5 or more characters!")
    while len(password) < password_length:
        print("Password too short")
        password = input("Enter password")
    return password


def print_asterisks(sequence):
    # Print asterisks equalling to the password count.
    print('*' * len(sequence))


main()
