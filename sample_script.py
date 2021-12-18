# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# init driver
driver = webdriver.Chrome(
    executable_path='C:\\Users\\zahid\\OneDrive\\Documents\\Automation\\python-selenium-automation\\chromedriver')
driver.maximize_window()

# implicit wait
# driver.implicitly_wait(4)

# explicit wait
driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
# sleep(4)

# click search
# driver.find_element(By.NAME, 'btnK').click()
element = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search button not found')
element.click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
