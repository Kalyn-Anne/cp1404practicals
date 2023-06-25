"""

QUESTIONS

1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
Remember to close your file.

2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above)
then prints,"Your name is Bob" (or whatever the name is in the file).

3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate
lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
which should be... 59.

4. Now write a fourth block of code that prints the total for all lines in numbers.txt
or a file with any number of numbers.

"""

# Question 1
OUTPUT_FILE = "name.txt"

name = input("Enter your name: ")
out_file = open(OUTPUT_FILE, 'w')
print(f"{name}", file=out_file)
out_file.close()
#
# # Question 2
in_file = open(OUTPUT_FILE, 'r')
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# Question 3
OUTPUT_FILE_2 = "numbers.txt"

in_file = open(OUTPUT_FILE_2, 'r')
total = 0
for i in range(0, 2):
    total = total + int(in_file.readline())
in_file.close()
print(f"{total}")

# Question 4
in_file = open(OUTPUT_FILE_2, 'r')
total = 0
for line in in_file:
    number = int(line)
    total = total + number
in_file.close()
print(f"{total}")
