from pytest_bdd import scenario, given, when, then


@given("the user is on the main page of Läslistan")
def step_main_page(page):
    page.goto("https://tap-vt26-testautomatisering.github.io/exam/")

@when("the user navigates to My Books and then returns to the Catalogue")
def step_open_catalogue(page):
    page.get_by_role("button", name="Mina böcker").click()
    page.get_by_role("button", name="Katalog").click()

@then("the page with the book list is opened")
def step_check_catalogue(page):
    assert page.locator(".book").count() > 0
    
@scenario("../../features/catalog.feature", "Open the book catalogue")
def test_open_catalogue():
    pass