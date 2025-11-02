# 4. Special/Magic Methods (Dunder Methods)
# Methods with double underscores __method__. They define how objects behave with built-in operations.
# Common special methods:

# __init__() - Constructor
# __str__() - String representation
# __repr__() - Official representation
# __len__() - Length
# __add__() - Addition operator
# __eq__() - Equality operator

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    # String representation
    def __str__(self):
        return f"Book: {self.title}"
    
    # Official representation 
    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"
    
    # Length operation
    def __len__(self):
        return self.pages
    
    # Addition operation 
    def __add__(self, other):
        total_pages = self.pages + other.pages
        return Book(f"{self.title} & {other.title}", total_pages)
    
    # Equality comparison
    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

book1 = Book("Python Basics", 300)
book2 = Book("Advanced Python", 500)

print(book1)                    # Output: Book: Python Basics (calls __str__)
print(repr(book1))              # Output: Book('Python Basics', 300)
print(len(book1))               # Output: 300 (calls __len__)

# Addition
combined = book1 + book2        # Calls __add__
print(combined.title)           # Output: Python Basics & Advanced Python
print(combined.pages)           # Output: 800

book3 = Book("Python Basics", 300)
print(book1 == book3)           