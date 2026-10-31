from behave import given, when, then


@given("the user is on the main page of Läslistan")
def step_main_page(context):
    context.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")


@when("the user navigates to My Books and then returns to the Catalogue")
def step_open_catalogue(context):
    context.page.get_by_role("button", name="Mina böcker").click()
    context.page.get_by_role("button", name="Katalog").click()


@then("the page with the book list is opened")
def step_check_catalogue(context):
    assert context.page.locator(".book").count() > 0
