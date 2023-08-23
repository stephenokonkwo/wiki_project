from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


# Allure command:
# python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/feature/test/

def browser_init(context):
    # """
    # :param context: Behave context
    # """

    ####  DEFAULT BROWSER: CHROME-CROSS BROWSER-  ####
    ## regular way
    # driver_path = ChromeDriverManager().install()
    # service = Service(executable_path=driver_path)

    # run on chrome for testing
    service = Service(executable_path='/Users/stephenokonkwo/Desktop/cureskin_project/chromedriver')

    context.driver = webdriver.Chrome(service=service)

    ####   FIREFOX-CROSS BROWSER   ####
    # context.driver = webdriver.Firefox(executable_path='')

    ####   SAFARI-CROSS BROWSER   ####
    # context.driver = webdriver.Safari()

    ####   HEADLESS MODE   ####
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ####   BROWSERSTACK   ####
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     'name': test_name
    # }
    # bs_user = ''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    #### MOBILE EMULATOR ####
    # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    #
    # chrome_options = webdriver.ChromeOptions()
    #
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
