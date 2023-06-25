import random

MAX_VALUE = 45
MIN_VALUE = 1
NUMBER_PER_LINE = 6


def main():
    number_quick_pick_rows = int(input("How many quick picks for generation: "))
    while number_quick_pick_rows <= 0:
        print("Invalid number of rows")
        number_quick_pick_rows = int(input("How many quick picks for generation: "))

    for i in range(0, number_quick_pick_rows):
        quick_pick = []

        for j in range(0, NUMBER_PER_LINE):
            number = random.randint(MIN_VALUE, MAX_VALUE)
            while number in quick_pick:
                number = random.randint(MIN_VALUE, MAX_VALUE)
            quick_pick.append(number)

        quick_pick.sort()

        print(" ".join(f"{number:2}" for number in quick_pick))


main()
