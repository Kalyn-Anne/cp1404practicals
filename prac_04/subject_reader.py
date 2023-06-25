"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data"


def main():
    subject_data = get_subjects()
    # print(subject_data)
    print_subjects(subject_data)


def get_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        subject.append(parts)
    input_file.close()
    return subject


def print_subjects(subject_data):
    """Display data nicely."""
    for subject in subject_data:
        print("{} is taught by {:12} and has {:2} students".format(*subject))


main()
