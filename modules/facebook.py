import os
from .robot import Robot


class Facebook(Robot):
    def log_in(self):
        self.driver.get('https://facebook.com')
        self.driver.find_element_by_id('email').send_keys(
            os.environ['FACEBOOK_EMAIL'])
        self.driver.find_element_by_id('pass').send_keys(
            os.environ['FACEBOOK_PASS'])
        self.driver.find_element_by_id('loginbutton').click()
