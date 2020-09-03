HEX_COLOURS_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                     "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                     "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                     "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                     "aquamarine4": "#458b74", "azure1": "#f0ffff",
                     "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                     "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_name = input("Enter colour name: ")

while colour_name != "":
    if colour_name in HEX_COLOURS_CODES:
        print("The HEX for \"{}\" is {} ".format(colour_name, HEX_COLOURS_CODES[colour_name]))
    else:
        print("Invalid Colour name")
    colour_name = input("Enter Colour: ")