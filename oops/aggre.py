class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

libary = Library("Times of INDIA")

book1 = Book("Raheem ke do hai","By raheem")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

libary.add_books(book1)
libary.add_books(book2)

for book in libary.list_books():
    print(f"{book}")