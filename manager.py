def manager():
    while True:
        print("---Manager Menu---")
        print("1.Manage Customer")
        print("2.manage Menu")
        print("3.View Ingredient")
        print("4.Update Profile")
        choice=input("enter your choice:")
        if choice=="1":
            manage_customer()
        elif choice=="2":
            Manage_Menu()
        elif choice=="3":
            View_ingredient()
        elif choice=="4":
            Update_profile()
        elif choice=="5":
            break
        else:
            print("invalid number")

def manage_customer():
    while True:
        print("---Manage Customer Menu---")
        print("1. Add Customer's name")
        print("2. Delete Customer's Name")
        print("3. edit Customer")
        print("4. Log Out")
        choice=input("enter your choice:")
        if choice=="1":
            add()
        elif choice=="2":
            Delete()
        elif choice=="3":
            edit()
        elif choice=="4":
            break
        else:
            print("invalid number")

def add():
    with open("customer.txt","a")as file:
        name=input("enter your name:")
        email=input("enter your email:")
        phone=int(input("enter your phone:"))
        file.write(f"{name},{email},{phone}\n")
        print("customer added successfully")


def Delete():
    print("\n")
    choice=input("Enter the name of the customer you want to delete:")
    with open("customer.txt","r") as file:
        document=file.readlines()
    with open("customer.txt","w") as file:
        for line in document:
            if choice not in line:
                file.write(line)
    print("Customer deleted successfully")

def edit():
    print("\n")
    choice=input("enter the name of the customer you want to edit")
    with open("customer.txt","r") as file:
        document=file.readlines()
    with open("customer.txt","w") as file:
        for line in document:
            if choice not in line:
                file.write(line)
    name=input("enter name")
    email=input("enter email")
    phone=input("enter phone")
    with open("customer.txt","a") as file:
        file.write(f"{name},{email},{phone}\n")
        print("Customer updated successfuly")

def Manage_Menu():
    while True:
        print("\n")
        print("---Manage Menu---")
        print("1. add a new menu item")
        print("2. Edit menu item/price")
        print("3. Delete menu item/price")
        print("5. Exit()")
        choice=input("What operation you want to perform ?:")
        if choice=="1":
            Add_menu()
        elif choice=="2":
            Edit_menu()
        elif choice=="3":
            Delete_menu()
        elif choice=="4":
            break
        else:
            print("invalid choice")
def Add_menu():
        with open("menu.txt","a")as file:
            name=input("enter menu item's name:")
            category=input("enter the category of the menu:")
            price=float(input("enter the price of the menu:"))
            file.write(f"{name},{category},{price}\n")
            print("menu added successfully")

def Edit_menu():
    print("\n")
    choice=input("enter the name of the item you want to edit")
    with open("menu.txt","r") as file:
        document=file.readlines()
    with open("menu.txt","w") as file:
        for line in document:
            if choice not in line:
                file.write(line)
    name=input("enter name of the item")
    category=input("enter the category of the item")
    price=float(input("enter price of the item"))
    with open("menu.txt","a") as file:
        file.write(f"{name},{category},{price}\n")
        print("Menu updated successfuly")
        
def Delete_menu():
    print("\n")
    choice=input("Enter the menu item you want to delete")
    with open("menu.txt","r") as file:
        document=file.readlines()
    with open("menu.txt","w") as file:
        for line in document:
            if choice not in line:
                file.write(line)
        print("Menu item deleted successfully!")

def View_ingredient():
    print("---View Menu Items---")
    with open("menu.txt","r") as file:
        ingredients=file.read()
        print("\n---List of the Ingerdients---")
        print(ingredients)

def Update_profile():
    print("\n")
    choice=input("update your own profile")
    with open("profile.txt","r") as file:
        document=file.readlines()
    with open("profile.txt","w") as file:
        for line in document:
            if choice not in line:
                file.write(line)
    name=input("enter your name")
    email=input("enter your email")
    number=float(input("enter your number"))
    with open("profile.txt","a") as file:
        file.write(f"{name},{email},{number}\n")
        print("Profile updated successfully!")
manager()