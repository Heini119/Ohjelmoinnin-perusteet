########################################################
# Task A10_T5
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

def recursiveFactorial(PNum: int) -> int:

    if PNum == 0 or PNum == 1:
        return 1
    else:
        return PNum * recursiveFactorial(PNum - 1)


def main():
    print("Program starting.")
    
    try:
        user_input = input("Insert factorial: ")
        number = int(user_input)

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial {number}!")
            result = recursiveFactorial(number)
            print(f"{number} = {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

    print("Program ending.")


if __name__ == "__main__":
    main()
