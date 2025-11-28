########################################################
# Task A9_T4
# Developer Heini Käräjämäki
# Date 2025-11-27
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000


def collectCelsius():
    feed= input("Insert celsius: ")
    try:
        celsius = float(feed)
    except ValueError:
        raise ValueError(f"Could not convert string to float: '{feed}'")
    if not (TEMP_MIN <= celsius <= TEMP_MAX):
        raise Exception(f"{celsius} temperature out of range.")
    return celsius


def main() -> None:
    print("Program starting.")
    try:
        celsius = collectCelsius()
        print(f"You inserted {celsius} °C")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)

    print("Program ending.")

if __name__ == "__main__":
    main()