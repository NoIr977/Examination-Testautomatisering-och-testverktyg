from pytest_bdd import scenario, given, when, then


@given("the user is on the Add Book page")
def step_add_book_page(page):
    page.goto("https://tap-vt26-testautomatisering.github.io/exam/")
    page.get_by_role("button", name = "Lägg till bok").click()

@when('the user enters "Pride and Prejudice" as the title')
def step_add_book_title(page):
    page.get_by_label("Titel").fill("Pride and Prejudice")

@when('the user enters "Jane Austen" as the author')
def step_add_author(page):
    page.get_by_label("Författare").fill("Jane Austen")

@when('the user clicks the "Lägg till ny bok" button')
def step_complete_adding(page):
    page.get_by_role("button", name="Lägg till ny bok").click()

@when("the user navigates to the catalogue")
def step_navigates_to_catalogue(page):
    page.get_by_role("button", name="Katalog").click()


@then("the new book is visible in the catalogue")
def step_check_new_book(page):
    assert page.get_by_text("Pride and Prejudice").is_visible()


@scenario("../../features/add_book.feature", "Add a new book")
def test_book_is_added():
    pass