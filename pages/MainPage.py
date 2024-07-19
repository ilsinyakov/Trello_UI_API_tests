# from time import sleep
from allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ConfigProvider import ConfigProvider
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage:
    def __init__(self, driver: WebDriver, cloud_session_token: str) -> None:
        self.driver = driver
        self.url = ConfigProvider().get("ui", "main_page_url")
        self.cloud_session_token = cloud_session_token

    @step('Open main page')
    def go(self):
        self.driver.get(self.url)
        cookie = {
            'name': 'cloud.session.token', 'value': self.cloud_session_token
            }
        self.driver.add_cookie(cookie)

        header_avatar = None
        i = 0
        while header_avatar is None and i < 5:
            i += 1
            self.driver.refresh()
            try:
                header_avatar = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR,
                         '[data-testid="header-member-menu-avatar"]')
                         ))
            except TimeoutException:
                header_avatar = None

    @step('Create board')
    def create_board(self, name) -> None:
        create_board_button = self.driver.\
            find_element(By.CSS_SELECTOR, '[data-testid="create-board-tile"]')
        create_board_button.click()

        name_field = self.driver.\
            find_element(By.CSS_SELECTOR,
                         '[data-testid="create-board-title-input"]')
        name_field.send_keys(name)

        create_board_submit_button = self.driver.\
            find_element(By.CSS_SELECTOR,
                         '[data-testid="create-board-submit-button"]')
        create_board_submit_button.click()
