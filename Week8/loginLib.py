import hashlib

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    return hashlib.md5(password.encode()).hexdigest()
    


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(DELIMITER)
            if len(parts) >= 2 and parts[1] == PUsername:
                return False
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        user_count = sum(1 for _ in f)

    user_id = user_count + 1
    hashed_pw = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{user_id}{DELIMITER}{PUsername}{DELIMITER}{hashed_pw}\n")

    return True



def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    hashed_pw = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(DELIMITER)
            if len(parts) == 3:
                user_id, username, stored_pw = parts
                if username == PUsername and stored_pw == hashed_pw:
                    return True



def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(DELIMITER)
            if len(parts) >= 2 and parts[1] == PUsername:
                return [parts[0], parts[1]]


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    updated = False
    lines = []
    hashed_pw = hash_password(PNewPassword)

    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(DELIMITER)
            if len(parts) == 3 and parts[1] == PUsername:
                # Päivitetään salasana
                lines.append(f"{parts[0]}{DELIMITER}{parts[1]}{DELIMITER}{hashed_pw}\n")
                updated = True
            else:
                lines.append(line)

    if updated:
        with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
            f.writelines(lines)

    return updated
