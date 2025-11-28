########################################################
# Task A10_T2
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        number = int(line)
                        PValues.append(number)
                    except ValueError:
                        print(f"Invalid integer in file: {line}")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {PFilename}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return None


def sumOfValues(PValues: list[int]) -> int:
    Sum = 0
    for v in PValues:
        Sum += v
    return Sum


def productOfValues(PValues: list[int]) -> int:
    Product = 1
    for v in PValues:
        Product *= v
    return Product


def main() -> None:

    Values: list[int] = []

    print("Program starting.")

    Filename = input("Insert filename: ").strip()

    readValues(Filename, Values)

    Sum = sumOfValues(Values)

    Product = productOfValues(Values)

    print("# --- Sum of numbers --- #")
    print(Sum)
    print("# --- Sum of numbers --- #")

    print("# --- Product of numbers --- #")
    print(Product)
    print("# --- Product of numbers --- #")

    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
