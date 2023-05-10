from ManagerSetup import PasswordManager
from passGen import genPassword

def main():
    password = {
    }

    pm = PasswordManager()

    print("""Main Menu
    (1) Create new key
    (2) Load Existing Key
    (3) Create new password file
    (4) Load exisitng password file
    (5) Add new password
    (6) Get a password
    (q) Quit
    """)

    done = False

    while not done:

        choice = input("Enter Choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            subRot = False
            while not subRot:
                site = input("Enter the site: ")
                option = input("""Do you wish to enter your own password or generate one?
                (1) Own Password
                (2) Random
            """)
                if choice == "1":
                    password = input("Enter the password: ")
                elif choice == "2":
                    passowrd = genPassword()
                    print(f"Generated Password is {password}.")
                else:
                    print("Inavlid Option!")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("Enter site for password: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            Done = True
            print("Bye")
        else: 
            print("Invalid Choice!")

if __name__ == "__main__":
    main()