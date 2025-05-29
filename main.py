import os
import time

# this is the file path 
ADMIN_FILE = "admin.txt"
STAFF_FILE = "staff.txt"
SALES_FILE = "sales.txt"
FEEDBACK_FILE = "feedback.txt"
ORDERS_FILE = "orders.txt"
INGREDIENTS_FILE = "ingredients.txt"
PROFILE_FILE = "profile.txt"
CUSTOMER_FILE = "customer.txt"
MENU_FILE = "menu.txt"
USERS_FILE = "users.txt"


def initialize_files():
    if not os.path.exists(ADMIN_FILE):
        with open(ADMIN_FILE, "w") as f:
            pass
    if not os.path.exists(STAFF_FILE):
        with open(STAFF_FILE, "w") as f:
            pass
    if not os.path.exists(SALES_FILE):
        with open(SALES_FILE, "w") as f:
            pass
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w") as f:
            pass
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w") as f:
            pass
    if not os.path.exists(INGREDIENTS_FILE):
        with open(INGREDIENTS_FILE, "w") as f:
            pass
    if not os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "w") as f:
            pass
    if not os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, "w") as f:
            pass
    if not os.path.exists(MENU_FILE):
        with open(MENU_FILE, "w") as f:
            pass
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            f.write("admin,admin1233\n")
            f.write("manager,manager12333\n")
            f.write("chef,chef123333\n")
            f.write("customer,customer1233333\n")

# Common functions designing header
def print_header(title):
    print("\n" + "-" * 50)
    print(f"{title:^50}")
    print("-" * 50)

def verify_login(username, password):
    """Check if username and password match stored credentials"""
    if not os.path.exists(USERS_FILE):
        return None
        
    with open(USERS_FILE, "r") as file:
        for line in file:
            if "," in line:
                stored_user, stored_pass = line.strip().split(",")
                if stored_user == username and stored_pass == password:
                    return stored_user
    return None

# Admin part 
def initialize_admin():
    username = input("Set Username of Admin: ")
    password = input("Set Password of Admin: ")

    with open(ADMIN_FILE, "r") as adminData:
        lines = adminData.readlines()

    for line in lines:
        if " : " in line:
            existing_username = line.split(" : ")[0]
            if existing_username == username:
                print(f"Username '{username}' already exists.")
                return

    with open(ADMIN_FILE, "a") as adminData:
        adminData.write(f"{username} : {password}\n")
    print("Admin Username and Password set successfully!")

def add_staff():
    role = input("Enter role (Manager/Chef): ").strip().capitalize()
    if role not in ["Manager", "Chef"]:
        print("Invalid role. Please enter either 'Manager' or 'Chef'.")
        return
    name = input(f"Enter {role} Name: ").strip()

    with open(STAFF_FILE, "a") as staffData:
        staffData.write(f"{role} : {name}\n")
    print(f"{role} {name} added successfully.")

def view_sales_report():
    if not os.path.exists(SALES_FILE):
        print("No sales report available.")
        return

    with open(SALES_FILE, "r") as salesData:
        reports = salesData.readlines()

    if not reports:
        print("No sales data found.")
    else:
        print("\nSales Report:")
        print("Month | Chef | Total Sales | Items Sold")
        print("-" * 40)
        for report in reports:
            print(report.strip())

def add_sales_report():
    month = input("Enter the month (e.g., January, February): ").strip()
    chef_name = input("Enter Chef Name: ").strip()
    total_sales = input("Enter total sales amount: ").strip()
    items_sold = input("Enter number of items sold: ").strip()

    with open(SALES_FILE, "a") as salesData:
        salesData.write(f"{month} | {chef_name} | {total_sales} | {items_sold}\n")
    print("Sales report added successfully.")

def export_sales_report():
    if not os.path.exists(SALES_FILE):
        print("No sales report available.")
        return

    with open(SALES_FILE, "r") as salesData:
        reports = salesData.readlines()

    export_file = "exported_sales_report.txt"
    with open(export_file, "w") as exportData:
        exportData.writelines(reports)
    print(f"Sales report successfully exported to {export_file}")

def view_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        print("No feedback available.")
        return

    with open(FEEDBACK_FILE, "r") as feedbackData:
        feedbacks = feedbackData.readlines()

    if not feedbacks:
        print("No feedback found.")
    else:
        print("\nCustomer Feedback:")
        print("-" * 40)
        for feedback in feedbacks:
            print(feedback.strip())

def admin_menu():
    attempts = 3
    while attempts > 0:
        print_header("Admin Login")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if verify_login(username, password) == "admin":
            while True:
                print_header("Admin Menu")
                print("1. Update Admin Profile")
                print("2. Manage Staff")
                print("3. Sales Report Management")
                print("4. View Customer Feedback")
                print("5. Exit")

                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    initialize_admin()
                elif choice == "2":
                    add_staff()
                elif choice == "3":
                    sales_menu()
                elif choice == "4":
                    view_feedback()
                elif choice == "5":
                    print("Exiting the program.")
                    return
                else:
                    print("Invalid choice, please try again.")
            return
        
        attempts -= 1
        print(f"Invalid credentials. {attempts} attempts left.")
    
    print("Too many failed attempts. Returning to main menu.")

def sales_menu():
    while True:
        print_header("Sales Report Menu")
        print("1. Add Sales Report")
        print("2. View Sales Report")
        print("3. Export Sales Report")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_sales_report()
        elif choice == "2":
            view_sales_report()
        elif choice == "3":
            export_sales_report()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Chef part 
def view_orders():
    print_header("View Orders")
    try:
        with open(ORDERS_FILE, "r") as file:
            orders = file.readlines()
            if not orders:
                print("\nNo orders available.")
                return
            for order in orders:
                if "," in order:
                    order_data = order.strip().split(", ")
                    if len(order_data) >= 4:
                        order_id, customer_name, dish_name, status = order_data[:4]
                        print(f"Order ID: {order_id} | Customer: {customer_name} | Dish: {dish_name} | Status: {status}")
    except FileNotFoundError:
        print("⚠️ No orders file found.")

def update_order_status():
    print_header("Update Order Status")
    view_orders()
    order_id = input("Enter Order ID to update: ").strip()
    new_status = input("Enter new status (In Progress/Completed): ").strip().title()

    if new_status not in ["In Progress", "Completed"]:
        print("\n❌ Invalid status entered. Please enter 'In Progress' or 'Completed'.")
        return

    try:
        with open(ORDERS_FILE, "r") as file:
            orders = file.readlines()

        updated_orders = []
        order_found = False
        for order in orders:
            if "," in order:
                order_data = order.strip().split(", ")
                if len(order_data) >= 4 and order_data[0] == order_id:
                    order_data[3] = new_status  
                    order_found = True
                    updated_order = ", ".join(order_data)
                    updated_orders.append(updated_order)
                else:
                    updated_orders.append(order.strip())

        if order_found:
            with open(ORDERS_FILE, "w") as file:
                file.write("\n".join(updated_orders) + "\n")
            print(f"\n✅ Order {order_id} updated to {new_status}.")
        else:
            print(f"\n❌ Order {order_id} not found.")
    except FileNotFoundError:
        print("⚠️ No orders file found.")

def add_ingredient():
    print_header("Add Ingredient")
    ingredient_name = input("Enter ingredient name: ").strip()
    quantity = input("Enter quantity: ").strip()

    with open(INGREDIENTS_FILE, "a") as file:
        file.write(f"{ingredient_name}, {quantity}\n")
    print(f"\n✅ {ingredient_name} added to ingredients list.")

def edit_ingredient():
    print_header("Edit Ingredient")
    ingredient_name = input("Enter ingredient name to edit: ").strip()

    try:
        with open(INGREDIENTS_FILE, "r") as file:
            ingredients = file.readlines()

        updated_ingredients = []
        ingredient_found = False

        for ingredient in ingredients:
            if ", " in ingredient:
                name, quantity = ingredient.strip().split(", ", 1)
                if name == ingredient_name:
                    edit_choice = input("Do you want to edit the (n)ame, (q)uantity, or (b)oth? ").strip().lower()

                    if edit_choice == "n":
                        new_name = input("Enter new ingredient name: ").strip()
                        updated_ingredients.append(f"{new_name}, {quantity}")
                    elif edit_choice == "q":
                        new_quantity = input("Enter new quantity: ").strip()
                        updated_ingredients.append(f"{name}, {new_quantity}")
                    elif edit_choice == "b":
                        new_name = input("Enter new ingredient name: ").strip()
                        new_quantity = input("Enter new quantity: ").strip()
                        updated_ingredients.append(f"{new_name}, {new_quantity}")
                    else:
                        print("\n❌ Invalid choice.")
                        return

                    ingredient_found = True
                else:
                    updated_ingredients.append(ingredient.strip())

        if ingredient_found:
            with open(INGREDIENTS_FILE, "w") as file:
                file.write("\n".join(updated_ingredients) + "\n")
            print(f"\n✅ Ingredient '{ingredient_name}' updated successfully.")
        else:
            print(f"\n❌ Ingredient '{ingredient_name}' not found.")
    except FileNotFoundError:
        print("⚠️ No ingredients file found.")

def delete_ingredient():
    print_header("Delete Ingredient")
    ingredient_name = input("Enter ingredient name to delete: ").strip()

    try:
        with open(INGREDIENTS_FILE, "r") as file:
            ingredients = file.readlines()

        updated_ingredients = []
        ingredient_found = False
        for ingredient in ingredients:
            if ", " in ingredient:
                name, _ = ingredient.strip().split(", ", 1)
                if name != ingredient_name:
                    updated_ingredients.append(ingredient.strip())
                else:
                    ingredient_found = True

        if ingredient_found:
            with open(INGREDIENTS_FILE, "w") as file:
                file.write("\n".join(updated_ingredients) + "\n")
            print(f"\n✅ Ingredient {ingredient_name} deleted.")
        else:
            print(f"\n❌ Ingredient {ingredient_name} not found.")
    except FileNotFoundError:
        print("⚠️ No ingredients file found.")

def update_chef_profile():
    print_header("Update Chef Profile")
    name = input("Enter your name: ").strip()
    contact = input("Enter your contact number: ").strip()

    with open(PROFILE_FILE, "w") as file:
        file.write(f"Name: {name}\nContact: {contact}")
    print(f"\n✅ Profile updated successfully for {name}.")

def chef_menu():
    attempts = 3
    while attempts > 0:
        print_header("Chef Login")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if verify_login(username, password) == "chef":
            while True:
                print_header("Chef Menu")
                print("1. View Orders")
                print("2. Update Order Status")
                print("3. Request Ingredients")
                print("4. Update Own Profile")
                print("5. Logout")
                
                choice = input("\nEnter your choice: ").strip()

                if choice == "1":
                    view_orders()
                elif choice == "2":
                    update_order_status()
                elif choice == "3":
                    print("\n--- Ingredient Options ---")
                    print("1. Add Ingredient")
                    print("2. Edit Ingredient")
                    print("3. Delete Ingredient")
                    ingredient_choice = input("Enter your choice: ").strip()

                    if ingredient_choice == "1":
                        add_ingredient()
                    elif ingredient_choice == "2":
                        edit_ingredient()
                    elif ingredient_choice == "3":
                        delete_ingredient()
                    else:
                        print("❌ Invalid choice.")
                elif choice == "4":
                    update_chef_profile()
                elif choice == "5":
                    print("\n🚪 Logging out... Goodbye!")
                    break
                else:
                    print("❌ Invalid choice. Please try again.")
            return
        
        attempts -= 1
        print(f"Invalid credentials. {attempts} attempts left.")
    
    print("Too many failed attempts. Returning to main menu.")

# Customer parts
def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            data = file.read().strip().split("\n")
            if len(data) >= 3:
                return {"name": data[0], "phone": data[1], "address": data[2]}
    return {"name": "Guest", "phone": "N/A", "address": "N/A"}

def save_profile(profile):
    with open(PROFILE_FILE, "w") as file:
        file.write(f"{profile['name']}\n{profile['phone']}\n{profile['address']}")

def load_orders():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as file:
            return [tuple(line.strip().split(",")) for line in file.readlines() if line.strip()]
    return []

def save_orders(orders):
    with open(ORDERS_FILE, "w") as file:
        for item in orders:
            file.write(f"{item[0]},{item[1]}\n")

def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            return file.readlines()
    return []

def save_feedback(feedback):
    with open(FEEDBACK_FILE, "a") as file:
        file.write(feedback + "\n")

def load_menu():
    menu = {}
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, "r") as file:
            for line in file:
                if "," in line:
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        menu[parts[0]] = float(parts[2])
    return menu

def display_menu(menu):
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item}: RM{price:.2f}")
    print("\n")

def order_food(menu, orders):
    display_menu(menu)
    while True:
        item = input("Enter the food item to order (or type 'done' to finish): ").capitalize()
        if item == "Done":
            if not orders:
                print("No food ordered.")
            break
        elif item in menu:
            orders.append((item, str(menu[item])))
            print(f"{item} added to your order.")
        else:
            print("Invalid item. Please select from the menu.")

def edit_order(orders):
    if not orders:
        print("You have not ordered anything yet.")
        return
    
    print("\n--- Your Current Order ---")
    for idx, (item, price) in enumerate(orders, start=1):
        print(f"{idx}. {item} - RM{price}")
    
    choice = input("Enter the item number to remove (or 'done' to exit): ")
    if choice.lower() == "done":
        return
    try:
        index = int(choice) - 1
        if 0 <= index < len(orders):
            removed_item = orders.pop(index)
            print(f"Removed {removed_item[0]} from your order.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_order(orders):
    if not orders:
        print("You have not ordered anything yet.")
        return
    
    print("\n--- Your Order ---")
    total = sum(float(price) for _, price in orders)
    for item, price in orders:
        print(f"{item}: RM{price}")
    print(f"Total Bill: RM{total:.2f}")

def confirm_payment(orders):
    if not orders:
        print("You have no items to pay for.")
        return
    
    view_order(orders)
    confirm = input("Confirm payment? (yes/no): ").strip().lower()
    if confirm == "yes":
        print("Payment successful! Your order is confirmed. You can take your meal at the counter.")
    else:
        print("Payment canceled.")

def send_feedback():
    feedback = input("Enter your feedback for the administrator: ").strip()
    if feedback:
        save_feedback(feedback)
        print("Thank you for your feedback!")
    else:
        print("Feedback cannot be empty.")

def update_customer_profile(profile):
    print("\n--- Update Profile ---")
    profile["name"] = input("Enter your name: ").strip() or profile["name"]
    
    while True:
        phone = input("Enter your phone number (10 digits): ").strip()
        if phone.isdigit() and len(phone) == 10:
            profile["phone"] = phone
            break
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")
    
    profile["address"] = input("Enter your address: ").strip() or profile["address"]
    print("Profile updated successfully!\n")

def view_profile(profile):
    print("\n--- Your Profile ---")
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")
    print("\n")

def customer_menu():
    attempts = 3
    while attempts > 0:
        print_header("Customer Login")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if verify_login(username, password) == "customer":
            customer_profile = load_profile()
            customer_orders = load_orders()
            menu = load_menu()
            
            while True:
                print_header("Customer Menu")
                print("1. View Menu")
                print("2. Order Food")
                print("3. Edit Order")
                print("4. View Order Summary")
                print("5. Confirm Payment")
                print("6. Send Feedback")
                print("7. View Profile")
                print("8. Update Profile")
                print("9. Logout")
                
                choice = input("Select an option: ").strip()

                if choice == "1":
                    display_menu(menu)
                elif choice == "2":
                    order_food(menu, customer_orders)
                    save_orders(customer_orders)
                elif choice == "3":
                    edit_order(customer_orders)
                    save_orders(customer_orders)
                elif choice == "4":
                    view_order(customer_orders)
                elif choice == "5":
                    confirm_payment(customer_orders)
                elif choice == "6":
                    send_feedback()
                elif choice == "7":
                    view_profile(customer_profile)
                elif choice == "8":
                    update_customer_profile(customer_profile)
                    save_profile(customer_profile)
                elif choice == "9":
                    print("Logging out...")
                    time.sleep(1)
                    break
                else:
                    print("Invalid choice. Try again.")
            return
        
        attempts -= 1
        print(f"Invalid credentials. {attempts} attempts left.")
    
    print("Too many failed attempts. Returning to main menu.")

# Manager parts 
def manage_customer():
    while True:
        print_header("Manage Customer Menu")
        print("1. Add Customer")
        print("2. Delete Customer")
        print("3. Edit Customer")
        print("4. Return to Manager Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            edit_customer()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def add_customer():
    with open(CUSTOMER_FILE, "a") as file:
        name = input("Enter customer name: ").strip()
        email = input("Enter customer email: ").strip()
        phone = input("Enter customer phone: ").strip()
        file.write(f"{name},{email},{phone}\n")
        print("Customer added successfully")

def delete_customer():
    print("\nCurrent Customers:")
    with open(CUSTOMER_FILE, "r") as file:
        for line in file:
            print(line.strip())
            
    name = input("\nEnter the name of the customer to delete: ").strip()
    
    with open(CUSTOMER_FILE, "r") as file:
        customers = file.readlines()
    
    with open(CUSTOMER_FILE, "w") as file:
        deleted = False
        for customer in customers:
            if not customer.startswith(name + ","):
                file.write(customer)
            else:
                deleted = True
                
    if deleted:
        print("Customer deleted successfully")
    else:
        print("Customer not found")

def edit_customer():
    print("\nCurrent Customers:")
    with open(CUSTOMER_FILE, "r") as file:
        for line in file:
            print(line.strip())
            
    old_name = input("\nEnter the name of the customer to edit: ").strip()
    
    with open(CUSTOMER_FILE, "r") as file:
        customers = file.readlines()
    
    found = False
    for customer in customers:
        if customer.startswith(old_name + ","):
            found = True
            break
    
    if not found:
        print("Customer not found")
        return
    
    with open(CUSTOMER_FILE, "w") as file:
        for customer in customers:
            if not customer.startswith(old_name + ","):
                file.write(customer)
    
    name = input("Enter new name: ").strip()
    email = input("Enter new email: ").strip()
    phone = input("Enter new phone: ").strip()
    
    with open(CUSTOMER_FILE, "a") as file:
        file.write(f"{name},{email},{phone}\n")
    
    print("Customer updated successfully")

def manage_menu():
    while True:
        print_header("Manage Menu")
        print("1. Add Menu Item")
        print("2. Edit Menu Item")
        print("3. Delete Menu Item")
        print("4. View Menu Items")
        print("5. Return to Manager Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_menu_item()
        elif choice == "2":
            edit_menu_item()
        elif choice == "3":
            delete_menu_item()
        elif choice == "4":
            view_menu_items()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_menu_item():
    with open(MENU_FILE, "a") as file:
        name = input("Enter item name: ").strip()
        category = input("Enter item category: ").strip()
        price = input("Enter item price: ").strip()
        file.write(f"{name},{category},{price}\n")
        print("Menu item added successfully")

def edit_menu_item():
    print("\nCurrent Menu Items:")
    with open(MENU_FILE, "r") as file:
        for line in file:
            print(line.strip())
            
    old_name = input("\nEnter the name of the item to edit: ").strip()
    
    with open(MENU_FILE, "r") as file:
        items = file.readlines()
    
    found = False
    for item in items:
        if item.startswith(old_name + ","):
            found = True
            break
    
    if not found:
        print("Item not found")
        return
    
    with open(MENU_FILE, "w") as file:
        for item in items:
            if not item.startswith(old_name + ","):
                file.write(item)
    
    name = input("Enter new item name: ").strip()
    category = input("Enter new category: ").strip()
    price = input("Enter new price: ").strip()
    
    with open(MENU_FILE, "a") as file:
        file.write(f"{name},{category},{price}\n")
    
    print("Menu item updated successfully")

def delete_menu_item():
    print("\nCurrent Menu Items:")
    with open(MENU_FILE, "r") as file:
        for line in file:
            print(line.strip())
            
    name = input("\nEnter the name of the item to delete: ").strip()
    
    with open(MENU_FILE, "r") as file:
        items = file.readlines()
    
    with open(MENU_FILE, "w") as file:
        deleted = False
        for item in items:
            if not item.startswith(name + ","):
                file.write(item)
            else:
                deleted = True
                
    if deleted:
        print("Menu item deleted successfully")
    else:
        print("Menu item not found")

def view_menu_items():
    print("\n--- Menu Items ---")
    with open(MENU_FILE, "r") as file:
        for line in file:
            print(line.strip())

def view_ingredients():
    print("\n--- Ingredients ---")
    with open(INGREDIENTS_FILE, "r") as file:
        for line in file:
            print(line.strip())

def update_manager_profile():
    print_header("Update Manager Profile")
    name = input("Enter your name: ").strip()
    contact = input("Enter your contact number: ").strip()

    with open(PROFILE_FILE, "w") as file:
        file.write(f"Name: {name}\nContact: {contact}")
    print(f"\n✅ Profile updated successfully for {name}.")

def manager_menu():
    attempts = 3
    while attempts > 0:
        print_header("Manager Login")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if verify_login(username, password) == "manager":
            while True:
                print_header("Manager Menu")
                print("1. Manage Customers")
                print("2. Manage Menu")
                print("3. View Ingredients")
                print("4. Update Profile")
                print("5. Logout")
                
                choice = input("Enter your choice: ").strip()
                
                if choice == "1":
                    manage_customer()
                elif choice == "2":
                    manage_menu()
                elif choice == "3":
                    view_ingredients()
                elif choice == "4":
                    update_manager_profile()
                elif choice == "5":
                    print("\nLogging out... Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            return
        
        attempts -= 1
        print(f"Invalid credentials. {attempts} attempts left.")
    
    print("Too many failed attempts. Returning to main menu.")

# Main menu
def login_system():
    initialize_files()
    
    while True:
        print_header("Restaurant Management System")
        print("1. Admin Login")
        print("2. Manager Login")
        print("3. Chef Login")
        print("4. Customer Login")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            admin_menu()
        elif choice == "2":
            manager_menu()
        elif choice == "3":
            chef_menu()
        elif choice == "4":
            customer_menu()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    login_system()