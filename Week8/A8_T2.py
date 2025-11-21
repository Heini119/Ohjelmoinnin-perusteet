import A8_T2Lib

def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))

def askChoice() -> int:
    return int(input("Your choice: "))
    

def showOptions() -> None:
    print("Options: ")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            result = A8_T2Lib.add(a, b)
            print(f"{a} + {b} = {result}")

        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            result = A8_T2Lib.subtract(a, b)
            print(f"{a} - {b} = {result}")

        elif choice == 3:
            a = askValue("Insert multiplicant value: ")
            b = askValue("Insert multiplier value: ")
            result = A8_T2Lib.multiply(a, b)
            print(f"{a} * {b} = {result}")

        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            result = A8_T2Lib.divide(a, b)
            print(f"{a} / {b} = {result}")

        else:
            print("Invalid choice, please try again.")

    print("Program ending.")

if __name__ == "__main__":
    main()