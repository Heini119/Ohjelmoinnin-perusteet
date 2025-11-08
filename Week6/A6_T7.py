LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = '; '

def readFile(PFilename) -> str:
    Content = ''
    FileHandle = open(PFilename, 'r')
    Row = FileHandle.readline()
    while Row != '':
        Content = Content + Row
        Row = FileHandle.readline()
    FileHandle.close()
    return Content

def writeFile() -> None:
    return None

def appendToFile() -> None:
    return None

def rot() -> str:
    newContent = ''
    return newContent

def getLocation(LocationId):
    Location = "unknown"
    if LocationId == 1:
        Location = "Galba's palace"
    elif LocationId == 2:
        Location = "Otho's palace"
    elif LocationId == 3:
        Location = "Vitellius's palace"
    elif LocationId == 4:
        Location = "Vespasian's palace"
    elif LocationId == 0:
        Location = "Home"
    return Location


def main() -> None:
    print("Travel starting.")
    PlayerProgressFilename = "player_progress.txt"
    Progress = readFile(PlayerProgressFilename)
    LastProgress = Progress.strip().split('\n')[-1].split(DELIMITER)
    CurrentLocationId = int(LastProgress[0])
    CurrentLocation = getLocation(CurrentLocationId)
    NextLocationId = int(LastProgress[1])
    NextLocation = getLocation(NextLocationId)
    PassPhrase = LastProgress[2]

    print(f"Currently at {CurrentLocation}.")
    print(f"Travelling to {NextLocation}.")
    print(f"Arriving to the {NextLocation}.")
    print("Passing the guard at the entrance")
    return None


main()