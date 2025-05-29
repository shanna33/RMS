import os

ORDERS_FILE = "orders.txt"
INGREDIENTS_FILE = "ingredients.txt"
PROFILE_FILE = "chef_profile.txt"

def initialize_files():
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w") as file:
            pass
    if not os.path.exists(INGREDIENTS_FILE):
        with open(INGREDIENTS_FILE, "w") as file:
            pass
    if not os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "w") as file:
            pass

def print_header(title):
    print("\n" + "-" * 50)
    print(f"{title:^50}")
    print("-" * 50)

def view_orders():
    print_header("View Orders")
    try:
        with open(ORDERS_FILE, "r") as file:
            orders = file.readlines()
            if not orders:
                print("\nNo orders available.")
                return
            for order in orders:
                order_id, customer_name, dish_name, status = order.strip().split(", ")
                print(f"Order ID: {order_id} | Customer: {customer_name} | Dish: {dish_name} | Status: {status}")
    except FileNotFoundError:
        print("⚠️ No orders file found.")

def update_order_status():
    print_header("Update Order Status")
    order_id = input("Enter Order ID to update: ").strip()
    new_status = input("Enter new status (In Progress/Completed): ").strip()

    if new_status not in ["In Progress", "Completed"]:
        print("\n❌ Invalid status entered. Please enter 'In Progress' or 'Completed'.")
        return

    try:
        with open(ORDERS_FILE, "r") as file:
            orders = file.readlines()

        updated_orders = []
        order_found = False
        for order in orders:
            order_data = order.strip().split(", ")
            if order_data[0] == order_id:
                order_data[3] = new_status  
                order_found = True
            updated_orders.append(", ".join(order_data))

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
    
            parts = ingredient.strip().split(", ", 1)

            if len(parts) != 2:
                print(f"⚠️ Malformed line in ingredients file: {ingredient.strip()}")
                continue  

            name, quantity = parts

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
            name, _ = ingredient.strip().split(", ")
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

def update_profile():
    print_header("Update Chef Profile")
    name = input("Enter your name: ").strip()
    contact = input("Enter your contact number: ").strip()

    with open(PROFILE_FILE, "w") as file:
        file.write(f"Name: {name}\nContact: {contact}")
    print(f"\n✅ Profile updated successfully for {name}.")

def chef_menu():
    initialize_files()
    while True:
        print_header("Chef Menu")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. Request Ingredients ")
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
            update_profile()
        elif choice == "5":
            print("\n🚪 Logging out... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

chef_menu()