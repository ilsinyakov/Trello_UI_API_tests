from allure import step
# from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ConfigProvider import ConfigProvider


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.url = ConfigProvider().get("ui", "base_url")
        self.driver = driver

    @step('Go to auth page')
    def go(self):
        self.driver.get(self.url)

    @step('Log in')
    def login_as(self, email: str, password: str) -> None:
        user_name_field = self.driver.find_element(By.ID, 'username')
        user_name_field.send_keys(email)

        submit_button = self.driver.find_element(By.ID, 'login-submit')
        submit_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              'svg[role="presentation"]'))
            )

        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, 'login-submit')
        login_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '[href^="https://trello.com"]'))
            )

        trello_link = self.driver.\
            find_element(By.CSS_SELECTOR, '[href^="https://trello.com"]')
        trello_link.click()

    @step('Get current url')
    def get_current_url(self) -> str:
        return self.driver.current_url
