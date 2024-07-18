from allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

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
