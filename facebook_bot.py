import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bot():
    def __init__(self):
        self.url = 'https://facebook.com'
        self.gecko_path = os.getenv('FIREFOX_PATH', '.\geckodriver.exe')
        self.driver = webdriver.Firefox(
            executable_path=self.gecko_path)
        self.email = os.getenv('USER', 'user@example.com')
        self.password = os.getenv('PASSWORD', 'user@example.com')

    def log_in(self):
        self.driver.get(self.url)
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('pass').send_keys(self.password)
        try:
            self.driver.find_element_by_name('login').click()
        except:
            self.driver.find_element_by_id('loginbutton').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'userNav')))
        print('Logged in')
        # self.driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('task', help='login')
    parser.add_argument('--email', '--user', '-u')
    parser.add_argument('--password', '-p')
    args = parser.parse_args()

    if args.email:
        os.environ['USER'] = args.user
    if args.password:
        os.environ['PASSWORD'] = args.password

    if args.function == 'login':
        bot = Bot()
        bot.log_in()
    else:
        print('Nothing to do')
