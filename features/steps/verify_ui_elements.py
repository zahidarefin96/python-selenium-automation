from behave import then
from selenium.webdriver.common.by import By

TEXT = (By.XPATH, "//h1[contains(text(),'Hello. What can we help you with?')]")
BODY_LINKS = (By.XPATH, "//div[@class='a-section a-spacing-large ss-landing-container-wide']//a")
SEARCH_BOX = (By.XPATH, "//input[@id='helpsearch']")
BROWSE_HELP_LINKS = (By.XPATH, "//div[@class='csg-hover-box clearfix']//div[@class='csg-hover-box-categories']//a")


# this step is already defined in <cancelling_order_amazon.py> file
# @given('Open Amazon Help page')
# def open_amazon_help_page(context):
#     context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@then('Verify page opened successfully')
def verify_page_opened(context):
    actual_result = context.driver.find_element(*TEXT).text
    expected_result = "Hello. What can we help you with?"

    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'


@then('Verify there are {expected_count} links are shown in body')
def verify_body_links(context, expected_count):
    expected_count = int(expected_count)
    body_links_count = len(context.driver.find_elements(*BODY_LINKS))

    assert body_links_count == 9, f'expected {expected_count} links, but got {body_links_count}'


@then('Verify Search Box is present')
def search_box(context):
    search_box = context.driver.find_element(*SEARCH_BOX)
    print(search_box.is_displayed())
    print(search_box.is_enabled())


@then("Verify there are {expected_count} links are shown in 'Browse Help'")
def body_links_count(context, expected_count):
    expected_count = int(expected_count)
    browse_links_count = len(context.driver.find_elements(*BROWSE_HELP_LINKS))
    assert browse_links_count == 12, f'expected {expected_count} links, but got {body_links_count}'
