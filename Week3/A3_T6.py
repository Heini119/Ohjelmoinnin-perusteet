print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print()
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

Choice = input("Your choice: ")
print()
if (Choice == "1"):
    print("Length options: ")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")

    ChoiceL = input("Your choice: ")
    if (ChoiceL == "1"):
        Meters = float(input("Insert meters: "))
        Result = round(Meters / 1000, 1)
        print(f"{Meters} m is {Result} km")
        print()
        print("Program ending.")
    elif (ChoiceL == "2"):
        Kilo = float(input("Insert kilometers: "))
        Result = round(Kilo * 1000, 1)
        print(f"{Kilo} km is {Result} m")
        print()
        print("Program ending.")
    elif (ChoiceL == "0"):
        print("Exiting...")
        print()
        print("Program ending.")
    else:
        print("Unknown option.")
        print()
        print("Program ending.")

elif (Choice == "2"):
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")

    ChoiceW = input("Your choice: ")
    if (ChoiceW == "1"):
        Grams = float(input("Insert grams: "))
        Result = round(Grams/453.59, 1)
        print(f"{Grams} g is {Result} lb")
        print()
        print("Program ending.")
    elif (ChoiceW == "2"):
        Pounds = float(input("Insert pounds: "))
        Result = round(Pounds*453.59, 1)
        print(f"{Pounds} lb is {Result} g")
        print()
        print("Program ending.")
    elif (ChoiceW == "0"):
        print("Exiting...")
        print()
        print("Program ending.")
    else:
        print("Unknown option.")
        print()
        print("Program ending.")
elif (Choice == "0"):
    print("Exiting...")
    print()
    print("Program ending.")
else:
    print("Unknown option.")
    print()
    print("Program ending.")