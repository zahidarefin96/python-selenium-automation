from behave import when, then


# scenario 1

# @given("Open Amazon page")
# def open_amazon(context):
#     context.app.main_page.open_page()


@when("Click Amazon Orders link")
def click(context):
    context.app.header.click_return_order()


@then("Verify that {expected_result} page is opened")
def verify_search_result(context, expected_result):
    context.app.sign_in_page.verify_search_result(expected_result)


# scenario 2

# @given("Open Amazon page")
# def open_amazon(context):
#     context.app.main_page.open_page()


# @when("Click on cart icon")
# def click(context):
#     context.app.header.click_cart()


@then("Verify {expected_text} text present")
def verify_search_result(context, expected_text):
    context.app.cart_page.verify_cart_empty_text(expected_text)
