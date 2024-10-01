# Task 1: Formatting Flight Itineraries
# Define a function that allows the user to add an itinerary
def add_itinerary(itineraries):
    traveler_input = input("Enter the traveler's name: ").title()
    origin_input = input("Enter the flight's origin: ").title()
    destination_input = input("Enter the flight's destination: ").title()
    itinerary = (traveler_input, origin_input, destination_input)
    itineraries.append(itinerary)
    print("Flight added to itineraries.")

# Define a function that takes a list of tuples as an argument and returns a formatted string
def view_itineraries(itineraries):
    for i, itinerary in enumerate(itineraries):
        traveler_name, origin, destination = itinerary
        print(f"Itinerary {i + 1}: {traveler_name} - From {origin} to {destination}")

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

while True:
    print("\n1. Add flight to itineraries\n2. View all flight itineraries\n3. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_itinerary(itineraries)
    elif user_input == "2":
        view_itineraries(itineraries)
    elif user_input == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid input. Please try again.")