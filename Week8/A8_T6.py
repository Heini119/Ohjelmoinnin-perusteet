from drawLib import drawCircle, drawSquare, saveSvg, Drawing

def main() -> None:
    # Initialize the drawing object
    Dwg = Drawing(size=("500px", "500px"))
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert square')
                left = float(askValue1("Left edge position"))
                top = float(askValue1("Top edge position"))
                sideLength = float(askValue1("Side length"))
                color = askValue2("Fill color")
                strokeColor = askValue2("Stroke color")
                drawSquare(Dwg, left, top, sideLength, color, strokeColor)

            case 2:
                print('Insert circle')
                centerX = float(askValue1("Center X"))
                centerY = float(askValue1("Center Y"))
                radius = float(askValue1("Radius"))
                color = askValue2("Fill color")
                stroke = askValue2("Stroke color")
                drawCircle(Dwg, centerX, centerY, radius, color, stroke)

            case 3:
                filename = askValue2("Filename to save (e.g. output.svg)")
                confirm = askValue2("Confirm save? (y/n)")
                if confirm.lower() == "y":
                    saveSvg(Dwg, filename)
                    print(f"Drawing saved as {filename}")
                else:
                    print("Save cancelled.")

            case 0:
                print("Exiting program.\n")
                break

            case _:
                print("Invalid choice, try again.")

        print()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()
