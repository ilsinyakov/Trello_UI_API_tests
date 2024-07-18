from time import sleep
import allure
from allure import severity_level

from pages.MainPage import MainPage


@allure.feature('Board')
@allure.severity(severity_level.BLOCKER)
def test_create_board(browser, cloud_session_token):
    main_page = MainPage(browser, cloud_session_token)
    main_page.go()
    sleep(40)
