from behave import given, when, then


# Scenario 1

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


# Scenario 2

@when("Hover over language options")
def hover_lang(context):
    context.app.header.hover_lang()


@then("Verify Spanish option present")
def verify_spanish_lang(context):
    context.app.header.verify_spanish_language_present()


#  Scenario 3

@when("Select department by alias {department}")
def select_department(context, department):
    context.app.header.select_department(department)


@then("Verify {category} department is selected")
def verify_department(context, category):
    context.app.search_results_page.verify_correct_department(category)
