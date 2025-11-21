from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            username = askValue("username")
            password = askValue("password")
            if login(username, password):
                print("Login successful.")
                userMenu(username)
            else:
                print("Login failed.")
        elif choice == 2:
            username = askValue("username")
            password = askValue("password")
            if register(username, password):
                print("Registration successful.")
            else:
                print("Registration failed.")
        elif choice == 0:  
            break
        else:
            print("Invalid choice.")

def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()

        if choice == 1:  
            profile = viewProfile(PUsername)
            if profile:
                print(f"User ID: {profile[0]}, Username: {profile[1]}")
            else:
                print("Profile not found.")
        elif choice == 2:  
            new_password = askValue("new password")
            if change_password(PUsername, new_password):
                print("Password changed.")
            else:
                print("Password change failed.")
        elif choice == 0:  
            break
        else:
            print("Invalid choice.")


def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()