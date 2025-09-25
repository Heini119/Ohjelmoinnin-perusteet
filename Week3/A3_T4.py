print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")
print()
print("Options:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
Choice = int(input("Your choice: "))
Back = (Name[::-1])
First = (Name[0])
Length = int(len(Name))

if (Choice == 1):
    print(f"Welcome {Name}!")
elif (Choice == 2):
    print(f"Your name backwards is \"{Back}\"")
elif (Choice == 3):
    print(f"The first character in name \"{Name}\" is \"{First}\"")
elif (Choice == 4):
    print(f"There are {Length} characters in the name \"{Name}\"")

elif (Choice == 0):
    print("Exiting...")
else:
    print("Unknown option")
print("Program ending")