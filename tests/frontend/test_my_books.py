from pytest_bdd import scenario, given, when, then


@given("the user is on the Katalog page")
def step_main_page(page):
    page.goto("https://tap-vt26-testautomatisering.github.io/exam/")


@when('the user clicks the heart symbol for "Ormar på ett plan: En Python-berättelse"')
def step_choose_favorite_book(page):
    page.get_by_test_id("star-Ormar på ett plan: En Python-berättelse").click()

@then("the book is marked as a favorite")
def step_check_mark(page):
    heart = page.get_by_test_id("star-Ormar på ett plan: En Python-berättelse")
    assert "selected" in heart.get_attribute("class").split()

@when('the user navigates to "Mina böcker"')
def step_navigates_to_favorites(page):
    page.get_by_role("button", name="Mina böcker").click()


@then('the book "Ormar på ett plan: En Python-berättelse" is visible in the favorites list')
def step_check_favorite_book(page):
    assert page.get_by_text("Ormar på ett plan: En Python-berättelse").is_visible()


@scenario("../../features/my_books.feature", "Add a book to favorites")
def test_add_book_to_favorites():
    pass