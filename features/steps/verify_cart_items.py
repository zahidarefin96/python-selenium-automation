from behave import given, when, then
from selenium.webdriver.common.by import By

WATER_BOTTLE = (By.XPATH, "//input[@id='twotabsearchtextbox']")
SEARCH_ICON = (By.XPATH, "//input[@id='nav-search-submit-button']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART = (By.XPATH, "//input[@id='add-to-cart-button']")
CART_ICON = (By.XPATH, "//a[@id='nav-cart']")
CART_COUNT = (By.XPATH, "//span[@id='sc-subtotal-label-activecart']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/ref=nav_logo')


@when('Search for amazon basics water bottle')
def search_icon(context):
    context.driver.find_element(*WATER_BOTTLE).send_keys("amazon basics water bottle")


@when('Click search icon')
def search_icon_click(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on the first product')
def product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on Add to Cart icon')
def add_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()


@when('Open Cart page')
def open_cart_page(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify cart has {expected_count} item(s)')
def verify_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    expected_count = "Subtotal (1 item):"

    assert actual_count == expected_count, f'Error, actual {actual_count} did not match {expected_count}'
