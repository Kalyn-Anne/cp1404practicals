"""
emails
Estimate: 50 minutes
Actual:   57 minutes
"""


def main():
    email_to_name = {}
    email = input("Enter email: ")
    while email != "":
        generated_name = get_name_from_email(email)
        print(generated_name)
        name = get_valid_name(email, generated_name)
        email_to_name[email] = name
        email = input("Enter email: ")
    display_emails(email_to_name)


def display_emails(email_to_name):
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_valid_name(email, generated_name):
    response = input("Is this your name? [Y/n] ").upper()
    if response == "Y" or response == "" or response == "YES":
        name = generated_name
    else:
        name = input("Name: ").title()
    return name


def get_name_from_email(email):
    """ Need More practise with splitting (this took the longest
    and required help from solutions """
    email_name = email.split('@')[0]
    name_parts = email_name.split('.')
    name = " ".join(name_parts).title()
    return name


main()
