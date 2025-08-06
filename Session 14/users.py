# Creeaza o aplicatie care permite user registration (first name, last name, user, password, email)  si user login. Datele de inregistrare se salveaza intr-un fisier .csv.
# Utilizatorul se poate loga doar daca s-a inregistrat.
# Dupa logare user-ul are posibilitatea de afisare detalii -> first name, last name, e-mail.
# Optiunea de afisare detalii nu apare inainte de logare.


import csv

USER_CSV_FILE = "users.csv"


def user_register():
    user_dict = {}
    user_dict["first_name"] = input("Enter first name: ")
    user_dict["last_name"] = input("Enter last name: ")
    user_dict["username"] = input("Enter username: ")
    user_dict["password"] = input("Enter password: ")
    user_dict["email"] = input("Enter email: ")

    field_names = ["first_name", "last_name", "username", "password", "email"]

    with open(USER_CSV_FILE, "a", newline="") as csvfile:
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)

        csv_dict_writer.writerow(user_dict)


def user_login_normal():
    user_dict = {}
    user_dict["username"] = input("Enter username: ")
    user_dict["password"] = input("Enter password: ")

    with open(USER_CSV_FILE) as csvfile:
        csvreader = csv.reader(csvfile)

        for user in csvreader:
            if user[2] == user_dict["username"] and user[3] == user_dict["password"]:
                return user

    return None


def user_login_dict():
    user_dict = {}
    user_dict["username"] = input("Enter username: ") # inca una
    user_dict["password"] = input("Enter password: ")

    field_names = ["first_name", "last_name", "username", "password", "email"]

    with open(USER_CSV_FILE, newline="") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile, fieldnames=field_names)

        next(csv_dict_reader)

        for user in csv_dict_reader:
            if user["username"] == user_dict["username"] and user["password"] == user_dict["password"]:
                return user

    return None


def user_manager():
    user = None
    while True:
        print("""#######
What action do you want to run?
login: Login with username and password.
register: Register a new user.
details: Shows the current users details (first name, last name, email).
logout: Logout current user.
stop: Stop the program...""")
        user_command = input("Enter command: ").lower().strip()
        if user_command == "stop":
            print("Goodbye!")
            return
        elif user_command == "login":
            user = user_login_dict()
            if user is None:
                print("Invalid username or password...")
            else:
                print(f"Welcome, {user['first_name']} {user['last_name']}!")
        elif user_command == "register":
            if user is None:
                user_register()
                print("User created successfully!")
            else:
                print("You are already logged in!")
        elif user_command == "details":
            if user is None:
                print("You are not logged in yet...")
            else:
                print(f"""Details:
First name: {user['first_name']}
Last name: {user['last_name']}
Email: {user['email']}""")
        elif user_command == "logout":
            if user is None:
                print("You are not logged in yet...")
            else:
                user = None
                print("Logout successful!")
        else:
            print("Invalid command...")

        print("#######\n")


if __name__ == '__main__':
    user_manager()
