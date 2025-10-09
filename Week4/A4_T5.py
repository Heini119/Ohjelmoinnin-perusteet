print("Program starting.\n")
Start = int(input("Insert starting point: "))
Stop = int(input("Insert stopping point: "))
Inspect = int(input("Insert inspection point: "))

valid = True
if (Start >= Stop):
    print("Starting point value must be less than the stopping point value.")
    valid = False
if not (Start < Inspect < Stop):
    print("Inspection value must be within the range of start and stop.")
    valid = False

if valid:
    print("\nFirst loop - inspection with break:")
    for i in range(Start, Stop):
        if i == Inspect:
            break
        print(i, end=" ")
    print()
    
    print("Second loop - inspection with continue:")
    for i in range(Start, Stop):
        if i == Inspect:
            continue
        print(i, end=" ")

print()
print()
print("Program ending.")



