# ROOM PRICE LIST
rooms = {
    "Single": 800,
    "Double": 1200,
    "Family": 2000
}

# RECORD STORAGE
records = {}

# ----------- INPUT VALIDATION FUNCTIONS -------------

def get_int(prompt):
    """Safely get an integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_float(prompt):
    """Safely get a floating-point input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

# ----------- MAIN SYSTEM FEATURES -------------------

def display_room_menu():
    print("\n--- ROOM MENU ---")
    for r, p in rooms.items():
        print(f"{r} Room = ₱{p}")

def check_in():
    """Processes a customer's check-in transaction."""
    display_room_menu()

    name = input("\nCustomer name: ")
    contact = input("Contact number: ")
    check_in_date = input("Check-in date: ")
    check_out_date = input("Check-out date: ")
    days = get_int("Number of days: ")

    num_rooms = get_int("How many rooms would you like to book?: ")

    room_list = []
    total_price = 0

    for i in range(num_rooms):
        print(f"\nRoom {i+1}:")
        print("Available Types: Single / Double / Family")

        while True:
            room_type = input("Choose room type: ").title()
            if room_type in rooms:
                room_list.append(room_type)
                total_price += rooms[room_type] * days
                break
            else:
                print("Invalid room type. Try again.")

    print(f"\nTotal Price for all rooms: ₱{total_price}")

    dp_choice = input("Would you like to make a downpayment? (yes/no): ").lower()
    paid = get_float("Enter downpayment: ") if dp_choice == "yes" else 0

    balance = total_price - paid

    # Save data
    records[name] = {
        "contact": contact,
        "rooms": room_list,
        "days": days,
        "check_in": check_in_date,
        "check_out": check_out_date,
        "total": total_price,
        "paid": paid,
        "balance": balance
    }

    print("\nCheck-In Successful!\n")

def check_out():
    """Handles check-out and final payment."""
    name = input("Customer name: ")

    if name not in records:
        print("Record not found.\n")
        return

    info = records[name]

    print("\n--- RECEIPT ---")
    print("Customer:", name)
    print("Contact:", info["contact"])
    print("Rooms Booked:", ", ".join(info["rooms"]))
    print("Days:", info["days"])
    print("Check-in:", info["check_in"])
    print("Check-out:", info["check_out"])
    print("Total Amount:", info["total"])
    print("Downpayment:", info["paid"])
    print("Balance:", info["balance"])

    pay = get_float("\nEnter final payment: ")

    if pay >= info["balance"]:
        change = pay - info["balance"]
        print(f"\nPayment Accepted! Change: ₱{change}")
        print("Check-Out Complete. Thank you!")
        del records[name]
    else:
        print("Insufficient Payment.\n")

# ----------- MAIN LOOP --------------------

def main():
    while True:
        print("\n=== HOTEL SYSTEM ===")
        print("A. Check-In")
        print("B. Check-Out")
        print("C. Exit")

        choice = input("Choose: ").upper()

        if choice == "A":
            check_in()
        elif choice == "B":
            check_out()
        elif choice == "C":
            print("Exiting system...")
            break
        else:
            print("Invalid option.\n")

main()