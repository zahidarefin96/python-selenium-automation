from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(
    executable_path='C:\\Users\\zahid\\OneDrive\\Documents\\Automation\\python-selenium-automation\\chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# one way(preffered)
driver.find_element(By.XPATH, "//input[@id='helpsearch']").send_keys("Cancel order", Keys.ENTER)

# another way
# enterButton = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
# enterButton.send_keys("Cancel order")
# enterButton.send_keys(Keys.ENTER)

actual_result = driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]").text
expected_result = "Cancel Items or Orders"

assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'

driver.quit()
