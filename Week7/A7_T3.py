WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def readFile(Filename: str, Rows: list[str]) -> None:
     print(f"Reading file '{Filename}'.")
     Rows.clear()
     with open(Filename, "r", encoding="UTF-8") as f:
        for line in f:
            if line.strip():
                Rows.append(line.strip())
     
def analyzeTimestamps(Rows: list[str], Results: list[str]) -> None:
        print("Analyzing timestamps.")
        Results.clear()
        weekday_counts: list[int] = [0] * len(WEEKDAYS)

        for row in Rows:
          for i,day in enumerate(WEEKDAYS):
              if row.startswith(day): 
                weekday_counts[i] += 1

        Results.append("### Timestamps analysis ###")
        
        for i, day in enumerate(WEEKDAYS):
            Results.append(f" - {day} {weekday_counts[i]} stamps")
        Results.append("### Timestamps analysis ###")

        return None

def displayResults(Results: list[str]) -> None:
     print("Displaying results.")
     for line in Results:
        print(line)

        
def main():
    Rows: list[str] = []
    Results: list[str] = []
    print("Program starting.")
    Filename = input("Insert filename: ")

    readFile(Filename, Rows)
    analyzeTimestamps(Rows, Results)
    displayResults(Results)

    print("Program ending.")

if __name__ == "__main__" :
    main()