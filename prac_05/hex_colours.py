"""
CP1404/CP5632 Practical
Program that allows you to look up hexadecimal colour,
Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Asparagus": "#87a96b", "Beaver": "#9f8170", "Black Coffee": "#3b2f2f",
                  "Bone": "#e3dac9", "Boysenberry": "#873260", "Bubble Gum": "#ffc1cc", "Citron": "#9fa91f",
                  "Corn": "#fbec5d", "#Eggplant": "#614051"}
print(COLOUR_TO_CODE)
print(len(COLOUR_TO_CODE))

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter short state: ").title()

