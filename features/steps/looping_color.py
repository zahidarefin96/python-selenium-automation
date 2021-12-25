from behave import given, then
from selenium.webdriver.common.by import By

# B081YS2F7N page by using CSS_SELECTOR
COLOR_OPTIONS_1 = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLORS_1 = (By.CSS_SELECTOR, '#variation_color_name .selection')

# B07BJKRR25 page by using XPATH
COLOR_OPTIONS_2 = (By.XPATH, "//div[@id='variation_color_name']//li")
SELECTED_COLORS_2 = (By.XPATH, "//div[@id='variation_color_name']//span[@class='selection']")

# WholeFoods page
REGULAR_1 = (By.XPATH,
             "//span[@class='a-size-small a-color-tertiary wfm-sales-item-card__regular-price']//parent::div//preceding-sibling::div[2]/span")

REGULAR_2 = (By.XPATH,
             "//span[@class='a-size-small a-color-tertiary wfm-sales-item-card__regular-price']//parent::div//preceding-sibling::div[3]/span")


@given('Open Amazon product {product_id} page in B081YS2F7N')
def open_amazon_product(context, product_id):
    context.driver.get(f"https://www.amazon.com/dp/{product_id}")


@given('Open Amazon product {product_id} page in B07BJKRR25')
def open_amazon_product(context, product_id):
    context.driver.get(f"https://www.amazon.com/gp/product/{product_id}/")


@given('Open Amazon WholeFoods page')
def open_wholefoods_page(context):
    context.driver.get("https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz")


@then('Verify user can click through the colors in Scenario 1')
def verify_colors_1(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray', 'Green']
    colors = context.driver.find_elements(*COLOR_OPTIONS_1)

    # one-way of verification (preferred)
    for i in range(len(colors[:9])):
        colors[i].click()
        actual_colors = context.driver.find_element(*SELECTED_COLORS_1).text
        print(actual_colors)

        assert actual_colors == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_colors}'

    # alternative-way of verification
    # actual_colors = []
    # for color in colors:
    #     color.click()
    #     actual_colors += [context.driver.find_element(*SELECTED_COLORS_1).text]
    #     print(actual_colors)
    #
    # assert actual_colors == expected_colors, f'Expected {expected_colors}, but got {actual_colors}'


@then('Verify user can click through the colors in Scenario 2')
def verify_colors_2(context):
    expected_colors = ['Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Wash', 'Indigo Wash',
                       'Light Blue Vintage']
    colors = context.driver.find_elements(*COLOR_OPTIONS_2)

    for i in range(len(colors[:6])):
        colors[i].click()
        actual_colors = context.driver.find_element(*SELECTED_COLORS_2).text
        print(actual_colors)

        assert actual_colors == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_colors}'


@then("Verify that every product on the page has a text ‘Regular’ and the product name")
def verify_product(context):
    product_name_1 = context.driver.find_elements(*REGULAR_1)
    product_name_2 = context.driver.find_elements(*REGULAR_2)

    for elements in (product_name_1 and product_name_2):
        print(elements.text)

        assert elements, 'Expected non-empty product name'
