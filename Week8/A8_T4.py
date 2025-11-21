import A8_T4Lib

def main():
    timestamps: list[A8_T4Lib.datetime] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    A8_T4Lib.readTimestamps(filename, timestamps)

    while True:
        print("\nOptions:")
        print("1 - Calculate amount of timestamps during year")
        print("2 - Calculate amount of timestamps during month")
        print("3 - Calculate amount of timestamps during weekday")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            year = int(input("Insert year: "))
            count = A8_T4Lib.calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}")
        elif choice == "2":
            month = input("Insert month: ")
            count = A8_T4Lib.calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}")
        elif choice == "3":
            weekday = input("Insert weekday: ")
            count = A8_T4Lib.calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

    print("Program ending.")

if __name__ == "__main__":
    main()
