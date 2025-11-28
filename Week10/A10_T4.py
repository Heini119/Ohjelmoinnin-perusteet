########################################################
# Task A10_T4
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = 0
    while i < len(PLeft) and j < len(PRight):
        if (PLeft[i] <= PRight[j]) == PAsc:
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    PMerge.extend(PLeft[i:])
    PMerge.extend(PRight[j:])

def mergeSort(PValues: list[int], PAsc: bool = True) -> list[int]:
    if len(PValues) <= 1:
        return PValues
    mid = len(PValues) // 2
    left = mergeSort(PValues[:mid], PAsc)
    right = mergeSort(PValues[mid:], PAsc)
    merged: list[int] = []
    merge(left, right, merged, PAsc)
    return merged

def main():
    print("Program starting.")
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    try:
        with open(filename, "r") as f:
            raw_data = f.read().strip()
            tokens = raw_data.replace("\n", ",").split(",")
            values = [int(x.strip()) for x in tokens if x.strip()]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    print(f"Raw '{filename}' -> {', '.join(map(str, values))}")

    asc_sorted = mergeSort(values, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_sorted))}")

    desc_sorted = mergeSort(values, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_sorted))}")
    print("Program ending.")

if __name__ == "__main__":
    main()
