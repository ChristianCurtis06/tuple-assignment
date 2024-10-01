# Task 1: Library System Enhancement
# Define a function that inserts new books into 'library' while handling duplicates
def add_book(library):
    title_input = input("Enter the new book title: ").title()
    if any(title_input.lower() == book[0].lower() for book in library):
        print(f"'{title_input}' already exists in library. Please enter another book.")
    else:
        author_input = input("Enter the author: ").title()
        new_book = (title_input, author_input)
        library.append(new_book)
        print(f"'{title_input}' added to library.")

# Define a function that displays the entire 'library' of books in formatted strings
def display_library(library):
    for book in library:
        title, author = book
        print(f"Title: {title}, Author: {author}")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

while True:
    print("\n1. Add new book to library\n2. Display all books in library\n3. Exit")
    user_input = input("Enter an action: ")
    if user_input == "1":
        add_book(library)
    elif user_input == "2":
        display_library(library)
    elif user_input == "3":
        print("Exiting the system...")
        break
    else:
        print("Invalid input. Please try again.")