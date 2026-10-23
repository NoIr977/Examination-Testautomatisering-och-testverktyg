from src.book_store import BookStore

def test_add_book():
    store = BookStore()

    store.addBook("Jane Austen", "Pride and Prejudice")

    assert len(store.books) == 1
    assert store.books[0]["author"] == "Jane Austen"
    assert store.books[0]["title"] == "Pride and Prejudice"
    assert store.books[0]["id"] == 1

def test_add_two_books():
    store = BookStore()

    store.addBook("Jane Austen", "Sense and Sensibility")
    store.addBook("Charlotte Brontë", "Jane Eyre")

    assert len(store.books) == 2
    assert store.books[0]["author"] == "Jane Austen"
    assert store.books[0]["title"] == "Sense and Sensibility"
    assert store.books[0]["id"] == 1
    assert store.books[1]["author"] == "Charlotte Brontë"
    assert store.books[1]["title"] == "Jane Eyre"
    assert store.books[1]["id"] == 2

def test_empty_store():
    store = BookStore()
    assert len(store.books) == 0


def test_add_to_favorites():
    store = BookStore()
    store.addBook("Jane Austen", "Pride and Prejudice")
    store.toggleFavorite(1)

    assert store.books[0]["favorite"] == True


def test_remove_from_favorites():
    store = BookStore()
    store.addBook("Jane Austen", "Pride and Prejudice")
    store.toggleFavorite(1)
    assert store.books[0]["favorite"] == True

    store.toggleFavorite(1)
    assert store.books[0]["favorite"] == False

def test_toggle_nonexisting_id():
    store = BookStore()
    store.addBook("Jane Austen", "Sense and Sensibility")
    store.toggleFavorite(999)
    assert store.books[0]["favorite"] == False