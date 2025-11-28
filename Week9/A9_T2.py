########################################################
# Task A9_T2
# Developer Heini Käräjämäki
# Date 2025-11-27
########################################################

import sys

def main() -> None:
    print("Program starting.")

    try:
        exitCode = input("Insert exit code(0-255): ")
        code = int(exitCode)
        if code < 0 or code > 255:
            print("Error code")
            sys.exit(1)
        else:
            print("Clean exit")
            sys.exit(0)
    except EOFError:
        print("Error code")
        sys.exit(1)

    print("Program ending.")

if __name__ == "__main__":
    main()