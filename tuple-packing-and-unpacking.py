# Task 1: Customer Order Processing
# Define a function that allows the user to add a new order to 'orders'
def add_order(orders):
    try:
        customer_input = input("Enter customer's name: ").title()
        product_input = input("Enter ordered product: ").capitalize()
        quantity_input = int(input("Enter quantity of product(s): "))    
        new_order = (customer_input, product_input, quantity_input)
        orders.append(new_order)
        print(f"New order added to list.")
    except ValueError or UnboundLocalError:
        print("ValueError: Invalid input. Please enter a number for quantity.")

# Define a function that unpacks each 'order' tuple and prints the details in a formatted string
def display_orders(orders):
    for order in orders:
        customer, product, quantity = order
        print(f"Customer: {customer}, Product: {product}, Quantity: {quantity}")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
]

while True:
    print("\n1. Add new order\n2. Display all orders\n3. Exit")
    user_input = input("Enter an action: ")
    if user_input == "1":
        add_order(orders)
    elif user_input == "2":
        display_orders(orders)
    elif user_input == "3":
        print("Exiting the system...")
        break
    else:
        print("Invalid input. Please try again.")