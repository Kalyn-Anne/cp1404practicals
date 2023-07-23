from prac_07.project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
FILENAME = "projects.txt"


def main():
    display_menu()
    choice = input(">>> ").upper()
    projects = get_projects()
    while choice != "Q":
        if choice == "L":
            for projects in projects:
                print(f"{projects.name}, is complete:{projects.is_complete()}")
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


def get_projects():
    projects = []
    input_file = open(FILENAME)
    next(input_file)  # skips headers
    for line in input_file:
        line = line.strip()
        parts = line.split('\t')
        # print(parts) # makes sure parts are right
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        parts[3] = float(parts[3])  # Make the number an float (ignore PyCharm's warning)
        parts[-1] = int(parts[-1])  # Make the number an integer (ignore PyCharm's warning)
        projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[-1]))
    input_file.close()
    return projects


main()
