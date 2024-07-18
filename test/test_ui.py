import allure
from allure import severity_level

from pages import AuthPage
from pages import MainPage

def get_cloud_session_token(browser):
    auth_page = AuthPage(browser)
    auth_page.go()

    auth_page


@allure.feature('Board')
@allure.severity(severity_level.BLOCKER)
def test_create_board(browser, test_data: dict):

