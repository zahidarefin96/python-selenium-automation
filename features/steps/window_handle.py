from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Scenario 1
PRIVACY_LINK = (By.LINK_TEXT, "Privacy Notice")
PRIVACY_NOTICE = (By.XPATH, "//h1[contains(text(),'Amazon.com Privacy Notice')]")

# Scenario 2
TOP_LINKS = (By.CSS_SELECTOR, "#zg_header a")
HEADER = (By.CSS_SELECTOR, "#zg_banner_text")


# Scenario 1

@given("Open Amazon T&C page")
def open_page(context):
    context.driver.get(
        "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle
    print("Original window: ", context.original_window)


@when("Click on Amazon Privacy Notice link")
def click_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when("Switch to the newly opened window")
def new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then("Verify Amazon Privacy Notice page is opened")
def verify_amazon_privacy(context):
    actual_result = context.driver.find_element(*PRIVACY_NOTICE).text
    expected_result = "Amazon.com Privacy Notice"

    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'


@then("User can close new window and switch back to original")
def switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


# Scenario 2

@given('Open Amazon BestSellers page')
def open_amazon_bestsellers_page(context):
    # context.driver.get('https://www.amazon.com/gp/bestsellers/')
    # context.driver.refresh()
    context.app.bestsellers_page.open()


@then("click each top link and verifies that new page opens")
def click_thru_top(context):
    context.app.bestsellers_page.click_thru_top()
