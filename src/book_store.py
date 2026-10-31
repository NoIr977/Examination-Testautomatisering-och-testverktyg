class BookStore:
    def __init__(self, favorite_books):
        self.books = []
        self.favorite_books = favorite_books

    def addBook(self, author, title):
        book_id = len(self.books) + 1

        book = {
            "author": author,
            "title": title,
            "id": book_id,
            "favorite": False
        }

        self.books.append(book)

    def toggleFavorite(self, book_id):
        for book in self.books:
            if book_id == book["id"]:
                if not book["favorite"]:
                    self.favorite_books.add(book)
                else:
                    self.favorite_books.remove(book)