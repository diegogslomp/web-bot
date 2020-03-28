import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bot():
    def __init__(self):
        if 'FIREFOX_PATH' in os.environ:
            self.driver = webdriver.Firefox(
                executable_path=os.environ['FIREFOX_PATH'])
        else:
            self.driver = webdriver.Firefox()

    def log_in(self):

        self.driver.get('https://facebook.com')
        self.driver.find_element_by_name('email').send_keys(
            os.environ['FACEBOOK_EMAIL'])
        self.driver.find_element_by_name('pass').send_keys(
            os.environ['FACEBOOK_PASS'])
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
    parser.add_argument('function', help='login')
    parser.add_argument('--email', '--user', '-u', help='facebook email')
    parser.add_argument('--password', '-p', help='facebook pass')
    args = parser.parse_args()

    if args.email:
        os.environ['FACEBOOK_EMAIL'] = args.email
    if args.password:
        os.environ['FACEBOOK_PASS'] = args.password

    if args.function == 'login':
        bot = Bot()
        bot.log_in()
    else:
        print('Nothing to do')
