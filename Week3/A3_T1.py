print("Program starting.")
print("Insert two integers.")
x = int(input("Insert first integer: "))
y = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if x < y:
    print("Second integer is greater.")
elif x > y:
    print("First integer is greater.")
else:
    print("Integers are the same.")
print()
print("Adding integers together")
print(f"{x} + {y} = {x+y}")
print()
print("Checking the parity of the sum...")
if (x + y)% 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending")
