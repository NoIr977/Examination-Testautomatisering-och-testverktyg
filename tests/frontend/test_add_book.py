from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import expect
from pages.add_book_page import AddBookPage

@given("the user is on the Add Book page")
def step_add_book_page(page):
    page.goto("https://tap-vt26-testautomatisering.github.io/exam/")
    page.get_by_role("button", name = "Lägg till bok").click()

@when(parsers.parse("the user enters {titel} as the title"))
def step_add_book_title(page, titel):
    add_book_page = AddBookPage(page)
    add_book_page.enter_title(titel)

@when(parsers.parse('the user enters {author} as the author'))
def step_add_author(page, author):
    add_book_page = AddBookPage(page)
    add_book_page.enter_author(author)

@when('the user clicks the "Lägg till ny bok" button')
def step_complete_adding(page):
    add_book_page = AddBookPage(page)
    add_book_page.click_add_book()

@when("the user navigates to the catalogue")
def step_navigates_to_catalogue(page):
    page.get_by_role("button", name="Katalog").click()


@then(parsers.parse("the book {titel} by {author} is visible in the catalogue"))
def step_check_new_book(page, titel, author):
    book_text = f'"{titel}", {author}'
    expect(page.get_by_text(book_text)).to_be_visible()


@scenario("../../features/add_book.feature", "Add a new book")
def test_book_is_added():
    pass