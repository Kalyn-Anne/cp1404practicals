"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

"""LOOK BEFORE YOU LEAP"""
# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()


"""EASIER TO ASK FORGIVENESS THAN PERMISSION"""
state_code = input("Enter short state: ").upper()
try:
    while state_code != "":
        print(state_code, "is", CODE_TO_NAME[state_code])
        state_code = input("Enter short state: ").upper()
except KeyError:
    print("Invalid short state")
print("end")

# for code, name in CODE_TO_NAME.items():
#     print(f"{code:3} is {name}")
