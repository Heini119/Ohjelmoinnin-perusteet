DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

class DAY_USAGE:
    def __init__(self):
        self.usage = 0.0
        self.cost = 0.0

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

def analyseTimestamps(timestamps: list[TIMESTAMP], analysis: list[DAY_USAGE]) -> None:
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturnday', 'Sunday']
    for day in weekdays:
        usage = DAY_USAGE()
        for t in timestamps:
            if t.weekday == day:
                usage.usage += t.consumption
                usage.cost += t.consumption * t.price
        analysis.append(usage)

def displayAnalysis(analysis: list[DAY_USAGE]) -> None:
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturnday', 'Sunday']
    print("### Electricity consumption summary ###")
    for i in range(7):
        print(f" - {weekdays[i]} usage {analysis[i].usage:.2f} kWh, cost {analysis[i].cost:.2f} €")
    print("### Electricity consumption summary ###")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = []
    readTimestamps(filename, timestamps)
    print("Analysing timestamps.")
    analysis = []
    analyseTimestamps(timestamps, analysis)
    print("Displaying results.")
    displayAnalysis(analysis)
    print("Program ending.")

if __name__ == "__main__":
    main()
