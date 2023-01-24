from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def main():
    options = Options()
    # options.add_argument('--headless')

    with Firefox(options=options) as b:
        b.get("https://google.com")
        user = b.find_element(By.ID, "")
        user.send_keys("test")
        login = b.find_element(By.XPATH, "")
        login.submit()
        input("Waiting for input..")


if __name__ == "__main__":
    main()
