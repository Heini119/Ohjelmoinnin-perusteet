def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def askChoice():
    choice = input("Insert choice: ").strip()
    if not choice.isnumeric():
        print("Unknown option!")
        return None
    return int(choice)

def main():
    print("Program starting.")
    count = 0
    while True:
        showOptions()
        choice = askChoice()

        if choice is None:
            continue
        elif choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

    print("Program ending.")
main()
