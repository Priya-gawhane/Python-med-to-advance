# Problem
# Create a Book class for a library management system with the following requirements:
# Class Attributes:

# total_books - tracks the total number of books in the library (shared across all book instances)
# library_name - stores the name of the library (same for all books)

# Instance Attributes:

# title - the book's title
# author - the book's author
# isbn - the book's ISBN number
# is_available - boolean indicating if the book is available for borrowing (default: True)

# Methods:

# __init__() - initialize a book and increment the total_books counter
# borrow_book() - mark the book as unavailable if it's available, otherwise print "Book is already borrowed"
# return_book() - mark the book as available again
# get_info() - return a formatted string with all book details
# get_total_books() - class method that returns the total number of books in the library

# Tasks:

# Create at least 3 book objects
# Display the total number of books
# Borrow 2 books and try to borrow one of them again
# Return 1 book
# Display information of all books and their availability status

# Expected Output Example:
# Total books in Central Library: 3
# Borrowed: Python Programming
# Book is already borrowed
# Returned: Python Programming
# Book: Python Programming by John Doe (Available)
# Try implementing this to practice working with both class and instance attributes!RetryClaude can make mistakes. Please double-check responses.

class Book:
    total_books = 0
    library_name = "boring zone"

    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

        Book.total_books += 1 #incrementing books 

    def borrow_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Returned: {self.title}")
        else:
            print(f"Book was not borrowed: {self.title}")
    
    def get_info(self):
        """Return formatted book information"""
        status = "Available" if self.is_available else "Not Available"
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
    
    @classmethod
    def get_total_books(cls):
        """Return the total number of books in the library"""
        return f"Total books in {cls.library_name}: {cls.total_books}"


# Testing the Book class
print("=" * 60)
print("LIBRARY MANAGEMENT SYSTEM")
print("=" * 60)

# Task 1: Create at least 3 book objects
book1 = Book("Python Programming", "John Doe", "978-0-123456-78-9")
book2 = Book("Data Structures", "Jane Smith", "978-0-987654-32-1")
book3 = Book("Machine Learning", "Bob Johnson", "978-0-555555-55-5")

print("\n--- Books Created ---")

# Task 2: Display the total number of books
print(Book.get_total_books())

# Task 3: Borrow 2 books and try to borrow one of them again
print("\n--- Borrowing Books ---")
book1.borrow_book()
book2.borrow_book()
book1.borrow_book()  # Try to borrow the same book again

# Task 4: Return 1 book
print("\n--- Returning Books ---")
book1.return_book()

# Task 5: Display information of all books
print("\n--- All Books Information ---")
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())

print("\n--- Final Statistics ---")
print(Book.get_total_books())
print(f"Library Name: {Book.library_name}")



    