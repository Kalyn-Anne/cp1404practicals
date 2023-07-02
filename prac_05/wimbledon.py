"""
CP1404 Practical
"""
FILENAME = "wimbledon"


def main():
    file_information = get_file_information(FILENAME)
    print(file_information)
    process_file_information()
    display_results()


def process_file_information():
    pass


def display_results():
    pass


def get_file_information(filename):
    file_information = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() # removes first line
        for line in in_file:
            parts = line.strip().split(",")
            file_information.append(parts)
    return file_information


main()
