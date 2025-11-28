########################################################
# Task A10_T6
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

import copy
import time
from typing import Callable


def bubbleSort(PNums: list[int]) -> list[int]:
    """Bubble sort implementation"""
    arr = PNums[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quickSort(PNums: list[int]) -> list[int]:
    """Quick sort implementation"""
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    return quickSort(left) + middle + quickSort(right)


def readValues(PValues: list[int], filename: str) -> None:
    PValues.clear()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime


def saveResults(filename: str, results: list[str]) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for line in results:
                f.write(line + "\n")
        print(f"Results saved to '{filename}'")
    except Exception as e:
        print(f"Error saving results: {e}")

def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    dataset_name: str = ""

    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            dataset_name = input("Insert dataset filename: ")
            readValues(Values, dataset_name)

        elif choice == "2":
            if not Values:
                print("No dataset loaded. Please read values first.")
                continue

            print(f"Measured speeds for dataset '{dataset_name}':")
            builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))

            print(f" - Built-in sorted {builtin_time} ns")
            print(f" - Bubble sort {bubble_time} ns")
            print(f" - Quick sort {quick_time} ns")

            Results.clear()
            Results.append(f"Measured speeds for dataset '{dataset_name}':")
            Results.append(f" - Built-in sorted {builtin_time} ns")
            Results.append(f" - Bubble sort {bubble_time} ns")
            Results.append(f" - Quick sort {quick_time} ns")

        elif choice == "3":
            if not Results:
                print("No results to save. Please measure speeds first.")
                continue
            filename = input("Insert results filename: ")
            saveResults(filename, Results)

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

    Values.clear()
    Results.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()
