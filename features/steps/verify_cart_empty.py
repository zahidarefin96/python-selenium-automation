from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon Home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/ref=nav_logo')


@when('Click on Cart icon')
def click(context):
    context.driver.find_element(By.ID, "nav-cart").click()


@then('Verify cart is empty')
def verify(context):
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text
    expected_result = "Your Amazon Cart is empty"

    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'
