import db

def create_user():
    username = input("Username: ")
    password = input("Password: ")
    db.create_user(username, password)
    print("User created!")

def view_user():
    username = input("Username: ")
    user = db.get_user(username)
    if user:
        print(user)
    else:
        print("User not found")

def delete_user():
    username = input("Username: ")
    db.delete_user(username)
    print("User deleted!")


if __name__ == "__main__":
    while True:
        choice = input("======== 1.Create 2.View 3.Delete 4.Exit ==========\nChoice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            view_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            print("Thank you for using this app... Bubye...")
            break