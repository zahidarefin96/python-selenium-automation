from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.events import EventFiringWebDriver

from support.logger import logger, MyListener

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'mdzahidarefin_SsK0dY'
bs_pw = 'kAY72DWRs1Lf5xpkZqef'


# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ .\features\tests\feature-name.feature
# allure serve test_results/

def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    context.driver = webdriver.Chrome(
        executable_path='C:\\Users\\zahid\\OneDrive\\Documents\\Automation\\python-selenium-automation\\chromedriver')
    # context.driver = webdriver.Edge(
    #     executable_path='C:\\Users\\zahid\\OneDrive\\Documents\\Automation\\python-selenium-automation\\msedgedriver')
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.PhantomJS()

    # # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options,
    #                                   executable_path='C:\\Users\\zahid\\OneDrive\\Documents\\Automation\\python-selenium-automation\\chromedriver')

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(
    #     executable_path='C:\\Users\\zahid\\OneDrive\\Documents\\Automation\\python-selenium-automation\\chromedriver'),
    #                                       MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options,
    #                                                        executable_path='C:\\Users\\zahid\\OneDrive\\Documents\\Automation\\python-selenium-automation\\chromedriver'),
    #                                       MyListener())

    ### for browerstack ###
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'os': 'Windows',
    #     'os_version': '11',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)  # 100 ms
    context.driver.wait = WebDriverWait(context.driver, 10)  # 500 ms
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        # print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
