import requests
from allure import step
from time import sleep


class BoardsApi:
    def __init__(self, base_url: str, api_key: str, token: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.token = token

    @step('Create board by API')
    def create_board(self, board_name: str) -> dict:
        path = (
            f'{self.base_url}/boards/?name={board_name}'
            f'&key={self.api_key}&token={self.token}'
        )

        resp = requests.post(path)
        return resp.json()

    @step('Delete board by ID by API')
    def delete_board_by_id(self, board_id: str) -> int:
        path = (
            f'{self.base_url}/boards/'
            f'{board_id}?key={self.api_key}&token={self.token}'
        )

        resp = requests.delete(path)
        return resp.status_code

    @step('Delete board by name by API')
    def delete_board_by_name(self, board_name: str) -> int:
        board_list = self.get_board_list()

        for board in board_list:
            if board["name"] == board_name:
                board_id_to_delete = board["id"]

        return self.delete_board_by_id(board_id_to_delete)

    @step('Get board list by API')
    def get_board_list(self) -> list:
        path = (
            f'{self.base_url}/members/me/boards/'
            f'?key={self.api_key}&token={self.token}'
        )
        resp = requests.get(path)
        return resp.json()

    @step('Get lists on board by API')
    def get_lists_on_board(self, board_id: str) -> list:
        path = (
            f'{self.base_url}/boards/'
            f'{board_id}/lists?key={self.api_key}&token={self.token}'
        )
        resp = requests.get(path)
        return resp.json()

    def is_board_in_list(self, board_name: str) -> bool:
        sleep(2)  # too fast. API doesn't work so fast
        board_list = self.get_board_list()

        for board in board_list:
            if board["name"] == board_name:
                return True

        return False
