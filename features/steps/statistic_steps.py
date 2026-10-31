from behave import when, then


@when('the user navigates to "Statistik"')
def step_open_statistics(context):
    context.page.get_by_role("button", name="Statistik").click()


@then("the user can see statistics about how many books are in the list")
def step_check_book_count(context):
    assert context.page.get_by_test_id("book-count").is_visible()


@then("the user can see statistics about how many books are marked as favorites")
def step_check_stars_count(context):
    assert context.page.get_by_test_id("stars-count").is_visible()

