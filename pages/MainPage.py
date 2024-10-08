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

    @step('Create board by UI')
    def create_board(self, board_name: str) -> None:
        create_board_button = self.driver.\
            find_element(By.CSS_SELECTOR, '[data-testid="create-board-tile"]')
        create_board_button.click()

        name_field = self.driver.\
            find_element(By.CSS_SELECTOR,
                         '[data-testid="create-board-title-input"]')
        name_field.send_keys(board_name)

        create_board_submit_button = self.driver.\
            find_element(By.CSS_SELECTOR,
                         '[data-testid="create-board-submit-button"]')
        create_board_submit_button.click()

    @step('Open main page')
    def go(self):
        self.driver.get(self.url)
        cookie = {
            'name': 'cloud.session.token', 'value': self.cloud_session_token
            }
        self.driver.add_cookie(cookie)

        # refreshing page,
        # until cookies are added and the main page is displayed
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

    @step('Go to board')
    def go_to_board(self, board_name: str) -> None:
        board_link = self.driver.\
            find_element(By.XPATH, f'//div[@title="{board_name}"]/ancestor::a')
        board_link.click()

    def is_board_present(self, board_name: str) -> bool:
        board_name_elements = self.driver.\
            find_elements(By.XPATH, '//li/a/div/div/div')

        for board_name_element in board_name_elements:
            if board_name_element.text == board_name:
                return True

        return False
