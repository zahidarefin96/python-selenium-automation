from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Click on Search Help Library')
def click(context):
    context.driver.find_element(By.XPATH, "//input[@id='helpsearch']").click()


@when('Input Cancel order')
def input(context):
    context.driver.find_element(By.XPATH, "//input[@id='helpsearch']").send_keys("Cancel order", Keys.ENTER)


@then("Verify ‘Cancel Items or Orders’ text is present")
def verify(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]").text
    expected_result = "Cancel Items or Orders"

    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'
