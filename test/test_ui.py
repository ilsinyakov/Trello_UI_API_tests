# from time import sleep
import allure
from allure import severity_level
from allure import step

from pages.MainPage import MainPage
from pages.BoardPage import BoardPage


@allure.feature('Board')
@allure.severity(severity_level.BLOCKER)
def test_create_board(browser, cloud_session_token):
    main_page = MainPage(browser, cloud_session_token)
    main_page.go()

    board_name = 'Test_board_2000'
    main_page.create_board(board_name)

    board_page = BoardPage(browser, browser.current_url)

    with step('Check that new board name is present'):
        assert board_page.is_board_present(board_name), \
            'New board name is not present'
