def askWord():
    Word = input("Insert word: ")
    return Word

print("Program starting: ")
print("Options:")
print("1 - Insert word")
print("2 - Show current word")
print("3 - Show current word in reverse")
print("0 - Exit")

choice = input("Your choice: ")

if choice == 1:
    askWord()
    