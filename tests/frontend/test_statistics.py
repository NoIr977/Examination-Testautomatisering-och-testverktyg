from pytest_bdd import scenario, given, when, then


@given("the user is on the main page of Läslistan")
def step_main_page(page):
    page.goto("https://tap-vt26-testautomatisering.github.io/exam/")


@when('the user navigates to "Statistik"')
def step_open_statistics(page):
    page.get_by_role("button", name="Statistik").click()


@then("the user can see statistics about how many books are in the list")
def step_check_book_count(page):
    assert page.get_by_test_id("book-count").is_visible()


@then("the user can see statistics about how many books are marked as favorites")
def step_check_stars_count(page):
    assert page.get_by_test_id("stars-count").is_visible()

@scenario("../../features/statistics.feature", "View book statistics")
def test_view_statistics():
    pass