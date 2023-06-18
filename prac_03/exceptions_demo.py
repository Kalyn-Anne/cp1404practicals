"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the value of the input is not an int.
2. When will a ZeroDivisionError occur?
When the denominator input is 0, as division is impossible.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we could use a while loop to get a valid number without using except. This allows the user to
keep entering until something other than 0 is entered rather than end the code.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
