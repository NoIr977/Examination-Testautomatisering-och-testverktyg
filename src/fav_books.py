class FavoriteBooks:
    def __init__(self):
        self.favorite_books = []

    def add(self, book):
        self.favorite_books.append(book)
        book["favorite"] = True

    def remove(self, book):
        self.favorite_books.remove(book)
        book["favorite"] = False