from src.fav_books import FavoriteBooks

def test_add_favorite_book():
    favorite = FavoriteBooks()

    book = {
        "author": "Jane Austen",
        "title": "Pride and Prejudice",
        "id": 1,
        "favorite": False
    }

    favorite.add(book)
    assert len(favorite.favorite_books) == 1
    assert favorite.favorite_books[0] == book
    assert favorite.favorite_books[0]["favorite"] == True


def test_remove_favorite_book():
    favorite = FavoriteBooks()

    book1 = {
        "author": "Jane Austen",
        "title": "Sense and Sensibility",
        "id": 1,
        "favorite": False
    }
    book2 = {
        "author": "J. K. Rowling",
        "title": "Harry Potter and the Goblet of Fire",
        "id": 2,
        "favorite": False
    }

    favorite.add(book1)
    favorite.add(book2)

    favorite.remove(book1)

    assert len(favorite.favorite_books) == 1
    assert favorite.favorite_books[0] == book2
    assert book1["favorite"] == False
