

MIN_PASSWORD_LENGTH = 6


def main():
    password = get_valid_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_valid_password():
    password = input("Enter password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Password length invalid")
        password = input("Enter password: ")
    return password


main()
