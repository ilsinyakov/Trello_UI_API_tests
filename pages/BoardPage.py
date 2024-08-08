from time import sleep
from allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from ConfigProvider import ConfigProvider
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
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

    def is_card_present(self, card_name: str) -> bool:
        # waiting for the board page to load
        WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="board-name-display"]'))
                )
        try:
            card_name_element = self.driver.\
                find_element(By.CSS_SELECTOR, '[data-testid="card-name"]')
            if card_name_element.text == card_name:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def is_card_present_in_list(self, card_name: str, list_num: str) -> bool:
        # waiting for the board page to load
        WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="board-name-display"]'))
                )
        try:
            card_name_element = self.driver.\
                find_element(By.XPATH,
                             f'//li[@data-testid="list-wrapper"][{list_num}]/\
                                descendant::a[@data-testid="card-name"]')
            if card_name_element.text == card_name:
                return True
            else:
                return False
        except NoSuchElementException:
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

    @step('Update card by UI')
    def update_card(self, card_name: str, new_card_name: str) -> None:
        go_to_card_button = self.driver.\
            find_element(By.XPATH, f'//a[contains(text(), "{card_name}")]')
        with step('CLick on card'):
            go_to_card_button.click()
        with step('Enter new card name'):
            card_name_text_area = self.driver.\
                find_element(By.CSS_SELECTOR,
                             '[data-testid="card-back-title-input"]')
            card_name_text_area.clear()
            card_name_text_area.send_keys(new_card_name)
        with step('Click close icon'):
            close_icon = self.driver.\
                find_element(By.CSS_SELECTOR, '[data-testid="CloseIcon"]')
            close_icon.click()

    @step('Delete card by UI')
    def delete_card(self, card_name: str) -> None:
        go_to_card_button = self.driver.\
            find_element(By.XPATH, f'//a[contains(text(), "{card_name}")]')
        with step('CLick on card'):
            go_to_card_button.click()
        with step('Archive card'):
            archive_card_button = self.driver.\
                find_element(By.CSS_SELECTOR,
                             '[data-testid="card-back-archive-button"]')
            archive_card_button.click()
        with step('Delete card'):
            delete_card_button = self.driver.\
                find_element(By.CSS_SELECTOR,
                             '[data-testid="card-back-delete-card-button"]')
            delete_card_button.click()
        with step('Click submit delete button'):
            submit_button = self.driver.\
                find_element(By.CSS_SELECTOR, '[type="submit"]')
            submit_button.click()

    @step('Move card to another list')
    def move_card(self, card_name: str, list_num: str) -> None:
        card = self.driver.\
            find_element(By.XPATH, f'//a[contains(text(), "{card_name}")]')
        another_list = self.driver.\
            find_element(By.XPATH,
                         f'//li[@data-testid="list-wrapper"][{list_num}]')
        ActionChains(self.driver).drag_and_drop(card, another_list).perform()
