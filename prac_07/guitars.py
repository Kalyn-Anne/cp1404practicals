"""
Plan
open file
close file
add guitars to list in appropriate chunks
add __lt__ to guitar class
sort list
print each in order of year


Add program to ask user to enter new guitars
store in list as object of guitar
save guitars to file

TEST
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitar = get_guitars()
    for guitar in sorted(guitar):
        print(guitar)


def get_guitars():
    guitars = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[1] = int(parts[1])  # Make the number an integer (ignore PyCharm's warning)
        parts[-1] = float(parts[-1])  # Make the number an float (ignore PyCharm's warning)
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    input_file.close()
    return guitars


def user_add_guitar():
    pass


def save_to_file():
    pass


main()
