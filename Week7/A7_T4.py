DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            row = line.rstrip()
            if not row:
                continue
            columns = row.split(DELIMITER)
            timestamp = TIMESTAMP()
            timestamp.weekday = columns[0]
            timestamp.hour = columns[1]
            timestamp.consumption = float(columns[2])
            timestamp.price = float(columns[3])
            timestamps.append(timestamp)


def displayTimestamps(timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for t in timestamps:
        total = t.consumption * t.price
        print(f" - {t.weekday} {t.hour}, price {t.price:.2f} €, consumption {t.consumption:.2f} kWh, total {total:.2f} €")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = readTimestamps(filename)
    displayTimestamps(timestamps)
    print("Program ending.")

if __name__ == "__main__":
    main()

