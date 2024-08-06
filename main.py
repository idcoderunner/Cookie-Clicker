from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

# TODO: 1. Add save and load modules. Save after every long cycle and load at the beginning.


SINGLE_CLICKS_COUNT = 500
SHORT_CYCLE_COUNT = 20
LONG_CYCLE_COUNT = 100
PAUSE_BETWEEN_SHORT_CYCLES = 5
PAUSE_BETWEEN_LONG_CYCLES = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

try:
    lang = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
    lang.click()
except WebDriverException:
    time.sleep(2)
    lang = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
    lang.click()

time.sleep(2)
load_previous_game = driver.find_element(By.ID, value="prefsButton")
load_previous_game.click()
time.sleep(15)


big_cookie = driver.find_element(By.ID, value="bigCookie")
money = driver.find_element(By.ID, value="cookies").text


def click_big_cookie(times):
    for _ in range(times):
        cookie_clicker = driver.find_element(By.ID, value="bigCookie")  # Ensure the ID matches the actual element
        cookie_clicker.click()


def find_enabled():
    while True:
        try:
            products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
            product_to_buy = None
            for item in products:
                product_to_buy = item
            product_to_buy.click()
        except AttributeError:
            print("Let's bake more Cookies!")
            break


def run_cycle():
    for n in range(SHORT_CYCLE_COUNT + 1):
        click_big_cookie(SINGLE_CLICKS_COUNT)
        time.sleep(PAUSE_BETWEEN_SHORT_CYCLES)
        print(f'Short cycle number: {n} of {SHORT_CYCLE_COUNT}')


def bake(repeats):
    for _ in range(repeats):
        run_cycle()
        time.sleep(PAUSE_BETWEEN_LONG_CYCLES)
        find_enabled()
        print(f'Running cycle: {_}')


bake(LONG_CYCLE_COUNT)
