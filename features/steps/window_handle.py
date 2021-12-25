from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Scenario 1
PRIVACY_LINK = (By.LINK_TEXT, "Privacy Notice")
PRIVACY_NOTICE = (By.XPATH, "//h1[contains(text(),'Amazon.com Privacy Notice')]")

# Scenario 2
BEST_SELLERS_TITLE = (By.XPATH, "//span[@id='zg_banner_text']")

NEW_RELEASES_LINK = (By.LINK_TEXT, "New Releases")
NEW_RELEASES_TITLE = (By.XPATH, "//span[@id='zg_banner_text']")

MOVERS_SHAKERS_LINK = (By.LINK_TEXT, "Movers & Shakers")
MOVERS_SHAKERS_TITLE = (By.XPATH, "//span[@id='zg_banner_text']")

MOST_WISHED_FOR_LINK = (By.LINK_TEXT, "Most Wished For")
MOST_WISHED_FOR_TITLE = (By.XPATH, "//span[@id='zg_banner_text']")

GIFT_IDEAS_LINK = (By.LINK_TEXT, "Gift Ideas")
GIFT_IDEAS_TITLE = (By.XPATH, "//span[@id='zg_banner_text']")


@given("Open Amazon T&C page")
def open_page(context):
    context.driver.get(
        "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


# this step is already defined in verify_cart_count.py file
# @given('Open Amazon BestSellers page')
# def open_amazon_bestsellers_page(context):
#     context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
#     context.driver.refresh()


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


@then("click each top link and verifies that new page opens")
def click_link(context):
    # Best Sellers
    best_sellers_title = context.driver.find_element(*BEST_SELLERS_TITLE)
    print(best_sellers_title.text)
    assert "Amazon Best Sellers" in best_sellers_title.text

    # New Releases
    new_releases_link = context.driver.find_element(*NEW_RELEASES_LINK)
    new_releases_link.click()
    new_releases_title = context.driver.find_element(*NEW_RELEASES_TITLE)
    print(new_releases_title.text)
    assert "Amazon Hot New Releases" in new_releases_title.text

    # Movers & Shakers
    movers_shakers_link = context.driver.find_element(*MOVERS_SHAKERS_LINK)
    movers_shakers_link.click()
    movers_shakers_title = context.driver.find_element(*MOVERS_SHAKERS_TITLE)
    print(movers_shakers_title.text)
    assert "Amazon Movers & Shakers" in movers_shakers_title.text

    # Most Wished For
    most_wished_link = context.driver.find_element(*MOST_WISHED_FOR_LINK)
    most_wished_link.click()
    most_wished_title = context.driver.find_element(*MOST_WISHED_FOR_TITLE)
    print(most_wished_title.text)
    assert "Amazon Most Wished For" in most_wished_title.text

    # Gift Ideas
    gift_ideas_link = context.driver.find_element(*GIFT_IDEAS_LINK)
    gift_ideas_link.click()
    gift_ideas_title = context.driver.find_element(*GIFT_IDEAS_TITLE)
    print(gift_ideas_title.text)
    assert "Amazon Gift Ideas" in gift_ideas_title.text
