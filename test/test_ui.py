# from time import sleep
import allure
from allure import severity_level
from allure import step

from pages.MainPage import MainPage
from pages.BoardPage import BoardPage


@allure.feature('Board')
@allure.severity(severity_level.BLOCKER)
@allure.title('Test create board by UI')
def test_create_board(browser, cloud_session_token, board_api_client):
    main_page = MainPage(browser, cloud_session_token)
    main_page.go()

    board_name = 'Test_board_2002'
    main_page.create_board(board_name)

    board_page = BoardPage(browser, browser.current_url)

    with step('Check that new board name is present'):
        assert board_page.is_board_present(board_name), \
            'New board name is not present'

    status_code = board_api_client.delete_board_by_name(board_name)
    with step('Check that the created board has been deleted'):
        assert status_code == 200, 'The created board has not been deleted'


@allure.feature('Board')
@allure.severity(severity_level.CRITICAL)
@allure.title('Test delete board by UI')
def test_delete_board(browser, cloud_session_token, board_api_client):
    board_name = 'Board to delete'
    board_api_client.create_board(board_name)

    main_page = MainPage(browser, cloud_session_token)
    main_page.go()

    main_page.go_to_board(board_name)

    board_page = BoardPage(browser, browser.current_url)
    board_page.delete_board()

    main_page = MainPage(browser, browser.current_url)
    with step('Check that deleted board is not present on main page'):
        assert not main_page.is_board_present('board_name'), \
            'Deleted board is present on main page'


@allure.feature('Card')
@allure.severity(severity_level.BLOCKER)
@allure.title('Test create card by UI')
def test_create_card(browser, cloud_session_token, board_api_client):
    board_name = 'Board to create card'
    card_name = 'Test card 2222'
    # card_name = 'New test card'
    board_api_client.create_board(board_name)

    main_page = MainPage(browser, cloud_session_token)
    main_page.go()

    main_page.go_to_board(board_name)

    board_page = BoardPage(browser, browser.current_url)
    board_page.create_card(card_name)
