print("Program starting.")
print()
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
Choice = int(input("Your choice: "))

if (Choice == 1):
    Celc = float(input("Insert the amount of Celsius: "))
    Fahr = Celc * 1.8 + 32
    print(f"{round (Celc ,1)} °C equals to {round (Fahr, 1)} °F")
    print()
    print("Program ending.")
elif (Choice == 2):
    Fahr = float(input("Insert the amount of Fahrenheit: "))
    Celc = (Fahr - 32) / 1.8
    print(f"{round(Fahr, 1)} °F equals to {round(Celc, 1)} °C")
    print()
    print("Program ending.")
elif (Choice == 0):
    print("Exiting...")
    print()
    print("Program ending.")
