import allure
from selenium import webdriver
import pytest

from pages.AuthPage import AuthPage
from api.BoardsApi import BoardsApi
from api.CardsApi import CardsApi
from api.ListsApi import ListsApi
from ConfigProvider import ConfigProvider
from DataProvider import DataProvider


base_url = ConfigProvider().get("api", "base_url")
api_key = DataProvider().get("apiKey")
token = DataProvider().get("token")


@pytest.fixture
def browser():
    with allure.step('Open browser'):
        timeout = int(ConfigProvider().get("ui", "timeout"))
        browser = webdriver.Chrome()
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step('Close browser'):
        browser.quit()


@pytest.fixture
def board_api_client() -> BoardsApi:
    with allure.step('Create boards API client'):
        return BoardsApi(base_url, api_key, token)


@pytest.fixture
def card_api_client() -> CardsApi:
    with allure.step('Create cards API client'):
        return CardsApi(base_url, api_key, token)


@pytest.fixture
def list_api_client() -> ListsApi:
    with allure.step('Create lists API client'):
        return ListsApi(base_url, api_key, token)


@pytest.fixture
def test_data():
    return DataProvider()


@pytest.fixture(scope="session")
def cloud_session_token() -> str:
    timeout = int(ConfigProvider().get("ui", "timeout"))
    browser = webdriver.Chrome()
    browser.implicitly_wait(timeout)
    browser.maximize_window()

    email = DataProvider().get("email")
    password = DataProvider().get("password")

    auth_page = AuthPage(browser)
    auth_page.go()

    auth_page.login_as(email, password)

    return auth_page.get_cloud_session_token()
