print("Program starting.")
print()
print("Check multiplicative persistence.")

Num = int(input("Insert an integer: "))
Steps = 0

while Num >= 10:
    numerot = [int(x) for x in str(Num)]
    for i in range(len(numerot) - 1):
        print(numerot[i], "*", end=" ")
    
    print(numerot[-1], "=", end=" ")
    tulos = 1
    for x in numerot:
        tulos *= x

    print(tulos)
    Num = tulos
    Steps += 1

print("No more steps.")
print()
print(f"This program took {Steps} step(s)")
print()
print("Program ending.")


