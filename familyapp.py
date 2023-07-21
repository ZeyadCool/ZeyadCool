import getpass
import time

member_balance = 0  

def member():
    global member_balance  
    print("Thanks for signing up!")
    member_balance = float(input("Please enter your balance: "))  
    start()

def admin():
    global member_balance  
    print("Thanks for signing up!")
    time.sleep(1)
    print("Enter 'View' to View the memebers' balance")
    print("Enter 'Exit' to Exit")
    view_or_not = input("Would you like to view your member's balance? ")

    while view_or_not != 'View' and view_or_not != 'Exit':
        print("Invalid choice!")
    if view_or_not == '1':
        print("Member balance:", member_balance)  
    else:
        exit

def admin_code():
    admin_main_password ="AdminsAreCool"
    enter_admin_password = input("Enter the admin's password to create a new account: ")
    while enter_admin_password != admin_main_password:
        print("Invalid password! Please try again.")
        enter_admin_password = input("Enter the admin's password to create a new account: ")
    if enter_admin_password == admin_main_password:
        admin_signup()

# Function to sign up as admin
def admin_signup():
    username = input("Enter an admin username: ")
    password = getpass.getpass("Enter an admin password: ")
    with open("admins.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Admin created successfully!")

# Function to sign up as member
def member_signup():
    username = input("Enter a member username: ")
    password = getpass.getpass("Enter a member password: ")
    with open("members.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Member created successfully!")

# Function to login as admin
def admin_login():
    username = input("Enter your admin username: ")
    password = getpass.getpass("Enter your admin password: ")
    with open("admins.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                print("Admin login successful!")
                return True
    print("Invalid username or password")
    return False

# Function to login as member
def member_login():
    username = input("Enter your member username: ")
    password = getpass.getpass("Enter your member password: ")
    with open("members.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                print("Member login successful!")
                return True
    print("Invalid username or password")
    return False

def start():
    global member_balance  
    while True:
        print("1. Admin Signup")
        print("2. Member Signup")
        print("3. Admin Login")
        print("4. Member Login")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == "1":
            if admin_code():
                admin()
        elif choice == "2":
            member_signup()
        elif choice == "3":
            if admin_login():
                admin()
                break
        elif choice == "4":
            if member_login():
                member()
                continue
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")
start()
