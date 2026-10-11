class Book:

    def __init__(self, author, book_name):
        self.author = author
        self.book_name = book_name

    def __str__(self):
        return f"{self.author} {self.book_name}"

    def __eq__(self, other):
        return self.author == other.author and self.book_name ==  other.book_name

    def __lt__(self, other):
        return self.author < other.author and self.book_name < other.book_name

book1 = Book("Morgan housel", "Psychology of Money")
book2 = Book("Morgan housel", "Psychology of Money")

print(book1)
print(book1 < book2)