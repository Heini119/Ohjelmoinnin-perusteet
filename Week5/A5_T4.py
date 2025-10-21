def askDimension(prompt: str) -> float:
   Feed = float(input(f"Insert {prompt}: "))
   return Feed


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = Width * Height
   return Area

print("Program starting.")

Width = askDimension("width")
Height = askDimension("height")

Area = calcRectangleArea(Width, Height)

print("")
print(f"Area is {Area}²")
print("Program ending.")
