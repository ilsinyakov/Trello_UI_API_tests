import allure
from selenium import webdriver
import pytest
from api.BoardsApi import BoardsApi
from ConfigProvider import ConfigProvider
from DataProvider import DataProvider
# from time import sleep


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
    return BoardsApi(base_url, token)


@pytest.fixture
def board_api_client_no_auth() -> BoardsApi:
    return BoardsApi(base_url, '')


@pytest.fixture
def board_id_to_delete() -> str:
    api = BoardsApi(base_url, token)
    json = api.post_board('to_delete')
    return json["id"]


@pytest.fixture
def delete_board():
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardsApi(base_url, token)
    api.delete_board(dictionary.get("board_id"))


@pytest.fixture
def test_data():
    return DataProvider()
