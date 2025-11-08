def analyze_names(filename):
    print(f'Reading names from "{filename}".')
    print("Analysing names...")

    names = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                names.extend(name.strip() for name in line.split(';') if name.strip())

    name_lengths = [len(name) for name in names]
    name_count = len(names)
    shortest = min(name_lengths)
    longest = max(name_lengths)
    average = sum(name_lengths) / name_count

    report = (
        "#### REPORT BEGIN ####\n"
        f"Name count - {name_count}\n"
        f"Shortest name - {shortest} chars\n"
        f"Longest name - {longest} chars\n"
        f"Average name - {average:.2f} chars\n"
        "#### REPORT END ####"
    )

    print("Analysis complete!")
    print(report)


def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    analyze_names(filename)
    print("Program ending.")
if __name__ == "__main__":
    main()