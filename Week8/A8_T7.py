import math
import svgwrite

def draw_square(dwg):
    x = int(input("Top-left X: "))
    y = int(input("Top-left Y: "))
    side = int(input("Side length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    dwg.add(dwg.rect(insert=(x, y), size=(side, side),
                     fill=fill, stroke=stroke))

def draw_circle(dwg):
    cx = int(input("Center X: "))
    cy = int(input("Center Y: "))
    r = int(input("Radius: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    dwg.add(dwg.circle(center=(cx, cy), r=r,
                       fill=fill, stroke=stroke))

def draw_hexagon(dwg):
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = int(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    
    R = apothem / math.cos(math.radians(30))

    points = []
    
    for i in range(6):
        angle_deg = -30 + i * 60
        angle_rad = math.radians(angle_deg)
        x = cx + R * math.cos(angle_rad)
        y = cy + R * math.sin(angle_rad)
        points.append((round(x), round(y)))

    dwg.add(dwg.polygon(points=points, fill=fill, stroke=stroke))

def main():
    print("Program starting.")
    dwg = svgwrite.Drawing()

    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            draw_square(dwg)
        elif choice == "2":
            draw_circle(dwg)
        elif choice == "3":
            draw_hexagon(dwg)
        elif choice == "4":
            filename = input("Insert filename: ")
            print(f'Saving file to "{filename}"')
            proceed = input("Proceed (y/n)?: ")
            if proceed.lower() == "y":
                dwg.saveas(filename)
                print("Vector saved successfully!")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

    print("Program ending.")

if __name__ == "__main__":
    main()
