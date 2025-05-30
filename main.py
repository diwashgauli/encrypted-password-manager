from encryption import get_encryptor
import database


fernet = get_encryptor()

def add_password():
    app_name = input("Application Name: ")
    password = input("Password: ")
    encrypted = fernet.encrypt(password.encode())
    database.save_password(app_name, encrypted.decode())
    print("Saved.")


def main():
    while True:
        print("\n1. Add Password\n2. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
