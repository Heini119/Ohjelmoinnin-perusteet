print("Program starting.")
Num = int(input("Insert a positive integer: "))
if Num > 0:
    Steps = 0
    print(str(Num), end="")

    while Num != 1:
        if Num % 2 == 0:
            Num = (Num //2)
        else:
            Num = (3 * Num + 1)
        print(" -> " + str(Num), end="")
        Steps += 1
    print()
    print("Sequence had "+ str(Steps) + " total steps.")
    print()
    print("Program ending.")




