import time
import os

# The food menu
menu = {
    "Burger": 12,
    "Pizza": 20,
    "Pasta": 15,
    "Salad": 10,
    "Soda": 5
}

# File paths
ORDER_FILE = "orders.txt"
PROFILE_FILE = "profile.txt"
FEEDBACK_FILE = "feedback.txt"

# Load customer profile
def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            data = file.read().strip().split("\n")
            if len(data) == 3:
                return {"name": data[0], "phone": data[1], "address": data[2]}
    return {"name": "Guest", "phone": "N/A", "address": "N/A"}

# Save customer profile
def save_profile():
    with open(PROFILE_FILE, "w") as file:
        file.write(f"{customer_profile['name']}\n{customer_profile['phone']}\n{customer_profile['address']}")

customer_profile = load_profile()

# Load orders
def load_orders():
    if os.path.exists(ORDER_FILE):
        with open(ORDER_FILE, "r") as file:
            return [tuple(line.strip().split(",")) for line in file.readlines() if line.strip()]
    return []

# Save orders
def save_orders():
    with open(ORDER_FILE, "w") as file:
        for item, price in customer_orders:
            file.write(f"{item},{price}\n")

customer_orders = load_orders()
order_status = "Paid" if customer_orders else "Pending"

# Load feedback
def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            return file.readlines()
    return []

# Save feedback
def save_feedback(feedback):
    with open(FEEDBACK_FILE, "a") as file:
        file.write(feedback + "\n")

customer_feedback = load_feedback()

def display_menu():
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item}: RM{price}")
    print("\n")

def order_food():
    global order_status
    display_menu()
    while True:
        item = input("Enter the food item to order (or type 'done' to finish): ").capitalize()
        if item == "Done":
            if not customer_orders:
                print("No food ordered.")
            break
        elif item in menu:
            customer_orders.append((item, str(menu[item])))
            order_status = "Pending"
            save_orders()
            print(f"{item} added to your order.")
        else:
            print("Invalid item. Please select from the menu.")

def edit_order():
    if not customer_orders:
        print("You have not ordered anything yet.")
        return
    
    print("\n--- Your Current Order ---")
    for idx, (item, price) in enumerate(customer_orders, start=1):
        print(f"{idx}. {item} - RM{price}")
    
    choice = input("Enter the item number to remove (or 'done' to exit): ")
    if choice.lower() == "done":
        return
    try:
        index = int(choice) - 1
        if 0 <= index < len(customer_orders):
            removed_item = customer_orders.pop(index)
            save_orders()
            print(f"Removed {removed_item[0]} from your order.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_order():
    if not customer_orders:
        print("You have not ordered anything yet.")
        return
    
    print("\n--- Your Order ---")
    total = sum(int(price) for _, price in customer_orders)
    for item, price in customer_orders:
        print(f"{item}: RM{price}")
    print(f"Total Bill: RM{total}")
    print(f"Order Status: {order_status}\n")

def confirm_payment():
    global order_status
    if not customer_orders:
        print("You have no items to pay for.")
        return
    
    view_order()
    confirm = input("Confirm payment? (yes/no): ").strip().lower()
    if confirm == "yes":
        order_status = "Paid"
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

def update_profile():
    print("\n--- Update Profile ---")
    customer_profile["name"] = input("Enter your name: ").strip() or customer_profile["name"]
    
    while True:
        phone = input("Enter your phone number (10 digits): ").strip()
        if phone.isdigit() and len(phone) == 10:
            customer_profile["phone"] = phone
            break
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")
    
    customer_profile["address"] = input("Enter your address: ").strip() or customer_profile["address"]
    save_profile()
    print("Profile updated successfully!\n")

def view_profile():
    print("\n--- Your Profile ---")
    for key, value in customer_profile.items():
        print(f"{key.capitalize()}: {value}")
    print("\n")

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Menu")
        print("2. Order Food")
        print("3. Edit Order")
        print("4. View Order Summary")
        print("5. Confirm Payment")
        print("6. View Order Status")
        print("7. Send Feedback")
        print("8. View Profile")
        print("9. Update Profile")
        print("10. Logout")
        choice = input("Select an option: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            order_food()
        elif choice == "3":
            edit_order()
        elif choice == "4":
            view_order()
        elif choice == "5":
            confirm_payment()
        elif choice == "6":
            print(f"Order Status: {order_status}\n")
        elif choice == "7":
            send_feedback()
        elif choice == "8":
            view_profile()
        elif choice == "9":
            update_profile()
        elif choice == "10":
            print("Logging out...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Try again.")

print("Customer Logged In Successfully!")
customer_menu()
