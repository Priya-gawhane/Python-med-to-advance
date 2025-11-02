# Create a Book class with the following:

# Attributes: title, author, pages
# Methods:

# get_info() - prints book information
# is_long() - returns True if pages > 300, else False



# Create 2-3 book objects and test the methods.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        print(f"Book title is {self.title} and author is{self.author}")

    def is_long(self):
        if self.pages > 300:
            return 'True'
        else:
            return 'False'
        
book1 = Book('fairytale', 'cinderalla', 456)
book1.get_info()

print(book1.is_long())

book2 = Book('psyphy', 'priya', 459)
book2.get_info()

print(book2.is_long())