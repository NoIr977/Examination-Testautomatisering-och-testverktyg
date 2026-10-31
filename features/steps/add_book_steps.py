from behave import given, when, then
from playwright.sync_api import expect
from pages.add_book_page import AddBookPage

@given("the user is on the Add Book page")
def step_add_book_page(context):
    context.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")
    context.page.get_by_role("button", name = "Lägg till bok").click()

@when("the user enters {titel} as the title")
def step_add_book_title(context, titel):
    add_book_page = AddBookPage(context.page)
    add_book_page.enter_title(titel)

@when('the user enters {author} as the author')
def step_add_author(context, author):
    add_book_page = AddBookPage(context.page)
    add_book_page.enter_author(author)

@when('the user clicks the "Lägg till ny bok" button')
def step_complete_adding(context):
    add_book_page = AddBookPage(context.page)
    add_book_page.click_add_book()

@when("the user navigates to the catalogue")
def step_navigates_to_catalogue(context):
    context.page.get_by_role("button", name="Katalog").click()


@then("the book {titel} by {author} is visible in the catalogue")
def step_check_new_book(context, titel, author):
    book_text = f'"{titel}", {author}'
    expect(context.page.get_by_text(book_text)).to_be_visible()

