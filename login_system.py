# Simple Signup & Login System
# Made with Python - Dictionary + Function + Loop

users = {}

def signup(username, password):
    """Create a new user account"""
    users[username] = password
    return "Account created successfully!"

def login(username, password):
    """Check if username and password match"""
    if username in users and users[username] == password:
        return True
    else:
        return False

def main():
    while True:
        print("\n--- Welcome ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("What do you want to do? ")

        if choice == "1":
            u = input("Create Username: ")
            p = input("Create Password: ")
            print(signup(u, p))

        elif choice == "2":
            u = input("Enter Username: ")
            p = input("Enter Password: ")
            if login(u, p):
                print(f"Welcome back, {u}!")
                break
            else:
                print("Wrong username or password! Try again.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please choose 1, 2 or 3.")

if __name__ == "__main__":
    main()