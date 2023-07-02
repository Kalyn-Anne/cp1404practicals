"""
CP1404 Practical
"""
FILENAME = "wimbledon"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    records = get_records(FILENAME)
    print(records)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print(champion_to_count)
    print(countries)


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # removes first line of information in text file
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
