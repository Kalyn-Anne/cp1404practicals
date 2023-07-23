MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    display_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            display_menu()
            choice = input(">>> ").upper()
        if choice == "S":
            display_menu()
            choice = input(">>> ").upper()
        elif choice == "D":
            display_menu()
            choice = input(">>> ").upper()
        elif choice == "F":
            display_menu()
            choice = input(">>> ").upper()
        elif choice == "A":
            display_menu()
            choice = input(">>> ").upper()
        elif choice == "U":
            display_menu()
            choice = input(">>> ").upper()
        else:
            print("Choice error try again")
            display_menu()
            choice = input(">>> ").upper()
    print("Have a nice day! :)")


def display_menu():
    print(MENU)


main()
