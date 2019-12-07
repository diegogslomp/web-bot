import os
from selenium import webdriver


class Bot():
    def __init__(self):

        if 'FIREFOX_PATH' in os.environ:
            self.driver = webdriver.Firefox(
                executable_path=os.environ['FIREFOX_PATH'])
        else:
            self.driver = webdriver.Firefox()
