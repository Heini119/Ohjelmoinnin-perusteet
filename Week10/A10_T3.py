########################################################
# Task A10_T3
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

import sys
from A10_TLib import readValues, displayValues, bubbleSort

def main() -> None:
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    readValues(Filename, Values)

    print(f"Raw '{Filename}' -> ", end="")
    displayValues(Values, Horisontally=True)

    bubbleSort(Values, PAsc=True)
    print(f"Ascending '{Filename}' -> ", end="")
    displayValues(Values, Horisontally=True)

    bubbleSort(Values, PAsc=False)
    print(f"Descending '{Filename}' -> ", end="")
    displayValues(Values, Horisontally=True)

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()


