from time import sleep
from allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from ConfigProvider import ConfigProvider
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    @step('Delete board by UI')
    def delete_board(self) -> None:
        with step('Click menu button'):
            menu_button = self.driver.\
                find_element(By.CSS_SELECTOR, '[aria-label="Меню"]')
            menu_button.click()

        with step('Click close board button'):
            close_board_button = self.driver.\
                find_element(By.CLASS_NAME, 'js-close-board')
            close_board_button.click()

        with step('Click close board confirm button'):
            # waiting for confirm pop-up window to display
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                'pop-over-header-title'))
                                                )
            close_board_confirm_button = self.driver.\
                find_element(By.CSS_SELECTOR,
                             '[data-testid="close-board-confirm-button"]'
                             )
            close_board_confirm_button.click()

        with step('Click delete board button'):
            delete_board_button = self.driver.\
                find_element(By.CSS_SELECTOR,
                             '[data-testid="close-board-delete-board-button"]'
                             )
            delete_board_button.click()

    @step('Create card by UI')
    def create_card(self, card_name: str) -> None:
        with step('Click add card button'):
            sleep(3)
            add_card_button = self.driver.\
                find_element(By.XPATH,
                             '(//*[@data-testid="list-add-card-button"])[1]'
                             )
            add_card_button.click()
            sleep(3)

        with step('Fill card name text area'):
            card_name_text_area = self.driver.\
                find_element(By.CSS_SELECTOR,
                             '[data-testid="list-card-composer-textarea"]'
                             )
            card_name_text_area.send_keys(card_name)
            sleep(3)

        with step('Click submit button'):
            submit_button = self.driver.\
                find_element(By.CSS_SELECTOR,
                             '[data-testid=\
                                "list-card-composer-add-card-button"]'
                             )
            submit_button.click()
            sleep(3)
