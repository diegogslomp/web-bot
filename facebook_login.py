from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

if __name__ == "__main__":
    url = 'https://facebook.com'
    gecko_path = os.getenv('FIREFOX_PATH', '.\geckodriver.exe')
    browser = webdriver.Firefox(executable_path=gecko_path)
    email = os.getenv('EMAIL', 'user@example.com')
    password = os.getenv('PASSWORD', 'password')
    browser.get(url)
    browser.find_element_by_id('email').send_keys(email)
    browser.find_element_by_id('pass').send_keys(password)
    browser.save_screenshot('example.png')
    # Sometimes using geckodriver the layout changes
    try:
        browser.find_element_by_id('login_form').submit()
    except:
        browser.find_element_by_id('u_0_a').submit()
    # self.browser.quit()
