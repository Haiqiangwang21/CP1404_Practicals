
def main():
    email_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_dict[email] = name
        email = input("Email: ")

    for email, name in email_dict.items():
        print("{} ({})".format(name, email))


def get_name(email):
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name


main()
