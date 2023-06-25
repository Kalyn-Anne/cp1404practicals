MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print("To start please enter a score")
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_grade_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for checking your score with us!")


def get_valid_score():
    score = int(input("Enter score: "))
    while 100 < score > 0:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_grade_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * score)


main()
