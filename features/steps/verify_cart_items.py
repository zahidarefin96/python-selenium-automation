from behave import when, then


# @given('Open Amazon main-page')
# def open_amazon(context):
#     # context.driver.get('https://www.amazon.com/ref=nav_logo')
#     context.app.main_page.open_page()


@when('type in search {keyword}')
def search_icon(context, keyword):
    # context.driver.find_element(*SEARCH_BOX).send_keys("amazon basics water bottle")
    context.app.header.search_input(keyword)


# @when('Click search button')
# def search_icon_click(context):
#     # context.driver.find_element(*SEARCH_ICON).click()
#     context.app.header.click_search()

@when('Click on the first product')
def product(context):
    # context.driver.find_element(*PRODUCT_PRICE).click()
    context.app.product_search_page.click()


@when('Click on Add to Cart icon')
def add_cart(context):
    # context.driver.find_element(*ADD_TO_CART).click()
    context.app.product_search_page.add_cart_icon()


@when('Open Cart page')
def open_cart_page(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart()


@then('Verify cart has {expected_result} item(s)')
def verify_count(context, expected_result):
    # actual_count = context.driver.find_element(*ITEM_COUNT).text
    # expected_count = "Subtotal (1 item):"
    #
    # assert actual_count == expected_count, f'Error, actual {actual_count} did not match {expected_count}'

    context.app.cart_page.verify_search_result(expected_result)
