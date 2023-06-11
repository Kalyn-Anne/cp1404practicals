MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print("To start please enter a score")
    get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            get_valid_score()
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for checking your score with us!")


def get_valid_score():
    score = float(input("Enter score: "))
    while 100 < score > 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
