from behave import given, then
from selenium.webdriver.common.by import By

FOOTER_LINKS = (By.XPATH, "//td[@class='navFooterDescItem']//a")
BEST_SELLERS_HEADER_LINK = (By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']//a")


# this step is already defined in verify_cart_items.py file
# @given('Open Amazon main-page')
# def open_amazon_home_page(context):
#     context.driver.get('https://www.amazon.com/')

@given('Open Amazon best-sellers page')
def open_amazon_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.refresh()


@then('Verify footer has {expected_count} links')
def verify_link1(context, expected_count):
    expected_count = int(expected_count)
    footer_links_count = len(context.driver.find_elements(*FOOTER_LINKS))
    assert footer_links_count == 40, f'expected {expected_count} links, but got {footer_links_count}'


@then('Verify header has {expected_count} links')
def verify_link2(context, expected_count):
    expected_count = int(expected_count)
    header_links_count = len(context.driver.find_elements(*BEST_SELLERS_HEADER_LINK))

    assert header_links_count == 5, f'expected {expected_count} links, but got {header_links_count}'
