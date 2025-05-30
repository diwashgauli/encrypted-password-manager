from encryption import get_encryptor
import database


fernet = get_encryptor()

def add_password():
    service = input("Service name: ")
    password = input("Password: ")
    encrypted = fernet.encrypt(password.encode())
    database.save_password(service, encrypted.decode())
    print("Saved.")

def get_password():
    service = input("Service name: ")
    data = database.fetch_password(service)
    if data:
        decrypted = fernet.decrypt(data.encode()).decode()
        print("Password:", decrypted)
    else:
        print("Not found.")

def show_services():
    services = database.list_services()
    print("Saved services:")
    for s in services:
        print("-", s)

def main():
    while True:
        print("\n1. Add Password\n2. Get Password\n3. List Services\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            show_services()
        elif choice == "4":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
