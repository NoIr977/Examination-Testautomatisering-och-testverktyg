class BookStore:
    def __init__(self):
        self.books = []

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
                book["favorite"] = not book["favorite"]