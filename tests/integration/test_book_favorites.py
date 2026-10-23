from src.book_store import BookStore
from src.fav_books import FavoriteBooks

def test_add_book_to_favorites():
    favorite = FavoriteBooks()
    store = BookStore()

    store.addBook("Jane Austen", "Pride and Prejudice")
    book = store.books[0]
    favorite.add(book)
    assert store.books[0]["favorite"] == True
    assert len(favorite.favorite_books) == 1
    assert favorite.favorite_books[0] == book


def test_remove_book_from_favorites():
    favorite = FavoriteBooks()
    store = BookStore()

    store.addBook("Charlotte Brontë", "Jane Eyre")
    book = store.books[0]
    favorite.add(book)

    assert store.books[0]["favorite"] == True
    assert len(favorite.favorite_books) == 1
    assert favorite.favorite_books[0] == book
    favorite.remove(book)
    assert store.books[0]["favorite"] == False
    assert len(favorite.favorite_books) == 0