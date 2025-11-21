def read_values(filename: str) -> list[float]:
    values = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # skip empty rows
                    values.append(float(line))
    except FileNotFoundError:
        print("File not found.")
    return values

def calculate_sum(values: list[float]) -> float:
    return round(sum(values), 1)

def calculate_average(values: list[float]) -> float:
    if len(values) == 0:
        return 0.0
    return round(sum(values) / len(values), 1)

def menu():
    values = []
    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Read values")
        print("2 - Amount of values")
        print("3 - Calculate sum of values")
        print("4 - Calculate average of values")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            filename = input("Insert filename: ")
            values = read_values(filename)
        elif choice == "2":
            print("Amount of values", len(values))
        elif choice == "3":
            print("Sum of values", calculate_sum(values))
        elif choice == "4":
            print("Average of values", calculate_average(values))
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
    print("Program ending.")

if __name__ == "__main__":
    menu()
