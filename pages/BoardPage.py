# from time import sleep
# from allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from ConfigProvider import ConfigProvider
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException


class BoardPage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def is_board_present(self, board_name: str) -> bool:
        board_name_element = self.driver.\
            find_element(By.CSS_SELECTOR, '[data-testid="board-name-display"]')
        if board_name_element.text == board_name:
            return True
        else:
            return False
