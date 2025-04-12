import json
import os

# ---------------------- Configuration ----------------------

DATA_FILE = 'library.txt'  # File to store library data

# ---------------------- Data Handling ----------------------

def load_library():
    """Load library data from the file, creating a default file if needed."""
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        with open(DATA_FILE, 'w') as file:
            json.dump([], file)
        return []

    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_library(library):
    """Save the library data to the file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(library, file, indent=4)

# ---------------------- Book Operations ----------------------

def add_book(library):
    """Add a new book to the library."""
    print("\n📘 Add New Book")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'✅ Book "{title}" added successfully!')
    return library  # Return the updated library

def remove_book(library):
    """Remove a book by title."""
    print("\n❌ Remove Book")
    title = input("Enter the title of the book to remove: ").strip().lower()
    initial_count = len(library)

    updated_library = [book for book in library if book['title'].lower() != title]

    if len(updated_library) < initial_count:
        save_library(updated_library)
        print(f'✅ Book "{title}" removed successfully!')
        return updated_library
    else:
        print(f'⚠️ Book "{title}" not found in the library.')
        return library

def search_library(library):
    """Search for books by title or author and display full details."""
    print("\n🔍 Search Library")
    search_by = input("Search by 'title' or 'author': ").strip().lower()

    if search_by not in ['title', 'author']:
        print("❌ Invalid input. Please search by 'title' or 'author'.")
        return

    search_term = input(f"Enter {search_by}: ").strip().lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print(f"\n🔎 Found {len(results)} result(s):\n")
        for book in results:
            display_book(book)
    else:
        print(f'⚠️ No books found matching {search_by}: "{search_term}".')

def display_all_books(library):
    """Display all books in the library."""
    print("\n📚 All Books in Library")
    if not library:
        print("No books in the library yet.")
        return

    for book in library:
        display_book(book)

def display_book(book):
    """Print details of a single book."""
    status = "✅ Read" if book.get('read', False) else "❌ Not Read"
    print(f"- Title : {book.get('title', 'Unknown Title')}")
    print(f"  Author: {book.get('author', 'Unknown Author')}")
    print(f"  Year  : {book.get('year', 'Unknown Year')}")
    print(f"  Genre : {book.get('genre', 'Unknown Genre')}")
    print(f"  Status: {status}\n")

def display_statistics(library):
    """Show reading statistics."""
    print("\n📊 Library Statistics")
    total = len(library)
    read = sum(1 for book in library if book.get('read', False))
    unread = total - read
    percent_read = (read / total * 100) if total > 0 else 0

    print(f"Total books  : {total}")
    print(f"Books read   : {read}")
    print(f"Books unread : {unread}")
    print(f"Read percent : {percent_read:.2f}%")

# ---------------------- Main Menu ----------------------

def main_menu():
    """Run the main menu once and exit."""
    library = load_library()

    print("\n========== 📚 Personal Library Manager ==========")
    print("1. ➕ Add Book")
    print("2. ❌ Remove Book")
    print("3. 🔍 Search Library")
    print("4. 📖 View All Books")
    print("5. 📊 View Statistics")
    print("6. 🚪 Exit")
    print("===============================================\n")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        library = add_book(library)
    elif choice == '2':
        library = remove_book(library)
    elif choice == '3':
        search_library(library)
    elif choice == '4':
        display_all_books(library)
    elif choice == '5':
        display_statistics(library)
    elif choice == '6':
        exit_program(library)
    else:
        print("❌ Invalid choice. Please enter a number from 1 to 6.")

def exit_program(_):
    """Exit the program."""
    print("👋 Exiting Library Manager. Have a great day!")
    exit()

# ---------------------- Entry Point ----------------------

if __name__ == "__main__":
    main_menu()
