########################################################
# Task A9_T7
# Developer Heini Käräjämäki
# Date 2025-11-28
########################################################

import sys
import os

def showHelp() -> None:
    """Show usage instructions."""
    print("Invalid amount of arguments.")
    print("Usage: python {} <src_file> <dst_file>".format(sys.argv[0]))
    return None

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    """Copy file from source to destination with overwrite prompt."""
    Proceed = False  

    if os.path.exists(PDstFile):
        answer = input('File "{}" already exists. Overwrite? (y/n): '.format(PDstFile))
        if answer.lower() == "y":
            Proceed = True
        else:
            print("Copy aborted.")
    else:
        Proceed = True


    if Proceed:
        try:
            print('Copying file "{}" to "{}".'.format(PSrcFile, PDstFile))
            
            with open(PSrcFile, "rb") as src, open(PDstFile, "wb") as dst:
                while True:
                    chunk = src.read(4096)
                    if not chunk:
                        break
                    dst.write(chunk)
        except Exception as e:
            print("Error: Could not copy file. Reason:", e)
            sys.exit(-1)

def main() -> None:
    print("Program starting.")

    if len(sys.argv) != 3:
        showHelp()
        sys.exit(-1)

    SrcFile = sys.argv[1]
    DstFile = sys.argv[2]

    print('Source file "{}"'.format(SrcFile))
    print('Destination file "{}"'.format(DstFile))

    copyFile(SrcFile, DstFile)

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
