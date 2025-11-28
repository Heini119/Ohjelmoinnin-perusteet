########################################################
# Task A9_T5
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)

    try:
        value_float = float(Feed)

        if not value_float.is_integer():
            raise ValueError(f'"{value_float}" is non-numeric value.')

        value_int = int(value_float)

        if not (0 <= value_int <= 255):
            raise ValueError(f'Value "{value_int}" is out of the range 0-255')

        return value_int

    except ValueError as e:
        raise ValueError(f"Invalid input '{Feed}': {e}")


def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)


def main():
    print("Program starting.")

    try:
        red = askIntByte("Enter red (0–255): ")
        green = askIntByte("Enter green (0–255): ")
        blue = askIntByte("Enter blue (0–255): ")

        hex_color = createHex(red, green, blue)

        print(f"RGB: ({red}, {green}, {blue})")
        print(f"Hex: {hex_color}")
        print(f"Binary: {red:08b}, {green:08b}, {blue:08b}")

    except Exception as e:
        print(f"Error: {e}")
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()

