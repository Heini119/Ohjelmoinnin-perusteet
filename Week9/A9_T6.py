########################################################
# Task A9_T6
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")


def askChoice() -> int:
    try:
        choice = int(input("Your choice: "))
        return choice
    except ValueError:
        print("Unknown option!")
        return -1


def saveLines(PLines: list[str]) -> None:
    if not PLines:
        print("No lines to save.")
        return
    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="UTF-8") as f:
            f.writelines(PLines)
        PLines.clear()
    except OSError as e:
        print(f"Error saving file: {e}")




def insertLine(PLines: list[str]) -> None:
    line = input("Insert text: ")
    PLines.append(line)


def onInterrupt(PLines: list[str]) -> None:
    if not PLines:
        print("^CClosing suddenly.")
    else:
        print("^CKeyboard interrupt and unsaved progress!")
        try:
            choice = input("Save before quit(y/n)?: ").lower()
            if choice == "y":
                saveLines(PLines)
        except Exception as e:
            print(f"Error: {e}")


def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            elif Choice != -1:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    finally:
        Lines.clear()
        print("Program ending.")


if __name__ == "__main__":
    main()


