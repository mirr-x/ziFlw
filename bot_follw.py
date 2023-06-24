# Automations for getting followers on Twitter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the browser
browser = webdriver.Firefox()


def twiti():
    # Open Twitter login page
    browser.get('https://twitter.com/i/flow/login')

    # Find the body element
    t = browser.find_element(By.TAG_NAME, 'body')

    time.sleep(3)

    action = ActionChains(browser)
    action.click()
    action.perform()

    time.sleep(1)

    # Fill in login credentials
    t.send_keys(Keys.TAB)
    t.send_keys(Keys.TAB)
    t.send_keys(Keys.TAB)
    t.send_keys(Keys.TAB)
    t.send_keys(Keys.TAB)
    t.send_keys(Keys.TAB)
    time.sleep(1)
    t.send_keys('userName')  # enter your username
    time.sleep(1)
    t.send_keys(Keys.ENTER)
    time.sleep(1)
    t.send_keys('passWord')  # enter your password
    time.sleep(2)
    t.send_keys(Keys.ENTER)


twiti()

time.sleep(4)

# Go to like4like.org login page
browser.get('https://www.like4like.org/login/')

# Find login elements
username = browser.find_element(By.NAME, 'username')
password = browser.find_element(By.NAME, 'password')
login = browser.find_element(By.XPATH, '//span[@onclick="LoginFunctions();"]')

# Fill in login credentials
username.send_keys('userName')           # enter your username
password.send_keys('passWord')  # enter your password
time.sleep(1)
login.click()
time.sleep(1)

# new part 1
# Go to earn credits page
link0 = browser.find_element(
    By.XPATH, '//a[@href="https://www.like4like.org/earn-credits.php"]')
time.sleep(3)
link0.click()

# new part 2 select
# Select the feature
link1 = browser.find_element(By.NAME, 'select-feature')
time.sleep(3)
link1.click()

# new part 3 choosing Twitter
# Select Twitter
link2 = browser.find_element(By.XPATH, '//option[@value="twitter"]')
time.sleep(3)
link2.click()
time.sleep(5)


def floww():
    # new part 4 click at the button
    # Click the button
    link3 = browser.find_element(
        By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']")
    link3.click()
    time.sleep(5)

    # twitii ---- 5
    # Switch to the new tab
    taps = browser.window_handles
    browser.switch_to.window(taps[1])

    tito = browser.find_element(By.TAG_NAME, 'body')
    tito.send_keys(Keys.TAB)
    time.sleep(2)
    tito.send_keys(Keys.TAB)
    time.sleep(2)
    tito.send_keys(Keys.ENTER)
    time.sleep(1)

    browser.close()

    # Switch back to the main tab
    browser.switch_to.window(taps[0])

    # DONE button part 6
    time.sleep(2)
    bt = browser.find_element(
        By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[1]/a')

    bt.click()
    time.sleep(1)
    browser.refresh()


while True:
    time.sleep(2)
    floww()
