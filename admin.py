import os

admin_file = "admin.txt"
staff_file = "staff.txt"
sales_file = "sales.txt"
feedback_file = "feedback.txt"

def initialize_admin():
    """Sets or updates the admin profile."""
    try:
        username = input("Set Username of Admin: ").strip()
        password = input("Set Password of Admin: ").strip()

        if not username or not password:
            print("Username and password cannot be empty.")
            return False

        with open(admin_file, "w") as adminData:
            adminData.write(f"{username} : {password}\n")

        print("Admin profile updated successfully!")
        return True
    except Exception as e:
        print(f"Error initializing admin: {e}")
        return False

def update_admin_profile():
    """Updates the admin username or password."""
    try:
        if not os.path.exists(admin_file):
            print("Admin file not found. Initialize admin first.")
            return False

        with open(admin_file, "r") as adminData:
            credentials = adminData.readline().strip().split(" : ")

        if len(credentials) != 2:
            print("Invalid admin file format. Resetting admin credentials.")
            return initialize_admin()

        old_username, old_password = credentials
        username = input("Enter new Admin Username: ").strip()
        password = input("Enter new Admin Password: ").strip()

        if not username or not password:
            print("Username and password cannot be empty.")
            return False

        with open(admin_file, "w") as adminData:
            adminData.write(f"{username} : {password}\n")

        print("Admin profile updated successfully.")
        return True
    except Exception as e:
        print(f"Error updating admin profile: {e}")
        return False

def add_staff():
    """Adds a new Manager or Chef to the staff list."""
    try:
        role = input("Enter role (Manager/Chef): ").strip().capitalize()
        if role not in ["Manager", "Chef"]:
            print("Invalid role. Please enter 'Manager' or 'Chef'.")
            return False

        name = input(f"Enter {role} Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return False

        with open(staff_file, "a") as staffData:
            staffData.write(f"{role} : {name}\n")
        
        print(f"{role} {name} added successfully.")
        return True
    except Exception as e:
        print(f"Error adding staff: {e}")
        return False

def view_staff():
    """Displays all staff members."""
    try:
        if not os.path.exists(staff_file):
            open(staff_file, "w").close()

        if os.stat(staff_file).st_size == 0:
            print("No staff records available.")
            return False

        print("\nCurrent Staff List:")
        with open(staff_file, "r") as staffData:
            for line in staffData:
                print(line.strip())
        return True
    except Exception as e:
        print(f"Error viewing staff: {e}")
        return False

def view_sales_report():
    """Displays the sales report."""
    try:
        if not os.path.exists(sales_file):
            open(sales_file, "w").close()

        if os.stat(sales_file).st_size == 0:
            print("No sales report available.")
            return False

        print("\nSales Report:")
        print("Month | Chef | Total Sales | Items Sold")
        print("-" * 40)
        with open(sales_file, "r") as salesData:
            for line in salesData:
                print(line.strip())
        return True
    except Exception as e:
        print(f"Error viewing sales report: {e}")
        return False

def add_sales_report():
    """Adds a new sales report entry."""
    try:
        month = input("Enter the month (e.g., January, February): ").strip()
        chef_name = input("Enter Chef Name: ").strip()
        total_sales = input("Enter total sales amount: ").strip()
        items_sold = input("Enter number of items sold: ").strip()

        if not all([month, chef_name, total_sales, items_sold]):
            print("All fields are required.")
            return False

        with open(sales_file, "a") as salesData:
            salesData.write(f"{month} | {chef_name} | {total_sales} | {items_sold}\n")

        print("Sales report added successfully.")
        return True
    except Exception as e:
        print(f"Error adding sales report: {e}")
        return False

def view_customer_feedback():
    """Displays customer feedback."""
    try:
        if not os.path.exists(feedback_file):
            open(feedback_file, "w").close()

        if os.stat(feedback_file).st_size == 0:
            print("No customer feedback available.")
            return False

        print("\nCustomer Feedback:")
        with open(feedback_file, "r") as feedbackData:
            for line in feedbackData:
                print(line.strip())
        return True
    except Exception as e:
        print(f"Error viewing customer feedback: {e}")
        return False

def add_customer_feedback():
    """Allows customers to provide feedback."""
    try:
        feedback = input("Enter customer feedback: ").strip()
        
        if not feedback:
            print("Feedback cannot be empty.")
            return False

        with open(feedback_file, "a") as feedbackData:
            feedbackData.write(feedback + "\n")
        
        print("Thank you! Your feedback has been recorded.")
        return True
    except Exception as e:
        print(f"Error adding customer feedback: {e}")
        return False

def sales_menu():
    """Sales report management menu."""
    while True:
        print("\nSales Report Menu:")
        print("1. Add Sales Report")
        print("2. View Sales Report")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_sales_report()
        elif choice == "2":
            view_sales_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """Admin authentication and main menu."""
    # Ensure files exist
    for file in [admin_file, staff_file, sales_file, feedback_file]:
        if not os.path.exists(file):
            open(file, "w").close()

    attempts = 3
    while attempts > 0:
        try:
            admin_username = input("Enter Admin Username: ").strip()
            admin_password = input("Enter Admin Password: ").strip()

            # Check if admin file is empty or improperly formatted
            with open(admin_file, "r") as adminData:
                credentials = adminData.readline().strip().split(" : ")

            if len(credentials) != 2:
                print("Invalid admin file format. Please initialize admin first.")
                initialize_admin()
                continue

            username, password = credentials
            if admin_username == username and admin_password == password:
                while True:
                    print("\nAdmin Menu:")
                    print("1. Update Admin Profile")
                    print("2. Manage Staff")
                    print("3. Sales Report Management")
                    print("4. View Customer Feedback")
                    print("5. Exit")

                    choice = input("Enter your choice: ").strip()

                    if choice == "1":
                        update_admin_profile()
                    elif choice == "2":
                        print("\nStaff Management:")
                        print("1. Add Staff")
                        print("2. View Staff")
                        print("3. Return to Main Menu")

                        sub_choice = input("Enter your choice: ").strip()
                        if sub_choice == "1":
                            add_staff()
                        elif sub_choice == "2":
                            view_staff()
                        elif sub_choice == "3":
                            continue
                        else:
                            print("Invalid choice. Returning to main menu.")
                    
                    elif choice == "3":
                        sales_menu()
                    elif choice == "4":
                        view_customer_feedback()
                    elif choice == "5":
                        print("Exiting the program.")
                        return
                    else:
                        print("Invalid choice, please try again.")
                return

            print("Invalid username or password. Please try again.")
            attempts -= 1

        except FileNotFoundError:
            print("Admin file not found. Please initialize admin first.")
            initialize_admin()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("Too many incorrect attempts. Exiting.")

# Run the main menu
if __name__ == "__main__":
    main_menu()