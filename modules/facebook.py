import os
import argparse
from robot import Robot


class Facebook(Robot):
    def log_in(self):
        self.driver.get('https://facebook.com')
        self.driver.find_element_by_name('email').send_keys(
            os.environ['FACEBOOK_EMAIL'])
        self.driver.find_element_by_name('pass').send_keys(
            os.environ['FACEBOOK_PASS'])
        self.driver.find_element_by_id('loginbutton').click()


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
        robot = Facebook()
        robot.log_in()
    else:
        print('Nothing to do')
