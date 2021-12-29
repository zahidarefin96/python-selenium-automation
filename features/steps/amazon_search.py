from behave import given, when, then


@given("Open Amazon Page")
def open_amazon(context):
    # context.driver.get("https://www.amazon.com/")
    context.app.main_page.open_page()


@when("Search for {keyword}")
def search_amazon(context, keyword):
    # context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(keyword)
    context.app.header.search_input(keyword)


@when("Click search button")
def click_search_icon(context):
    # context.driver.find_element(By.ID, "nav-search-submit-button").click()
    context.app.header.click_search()


@then("Search results have {expected_result}")
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)
