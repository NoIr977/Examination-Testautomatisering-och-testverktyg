from pytest_playwright.pytest_playwright import page


class AddBookPage:
    def __init__(self, page):
        self.page = page


    def enter_title(self, title):
        self.page.get_by_label("Titel").fill(title)

    def enter_author(self, author):
        self.page.get_by_label("Författare").fill(author)

    def click_add_book(self):
        self.page.get_by_role("button", name="Lägg till ny bok").click()