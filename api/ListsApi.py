import requests
from allure import step


class ListsApi:
    def __init__(self, base_url: str, api_key: str, token: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.token = token

    @step("Get cards in list by API")
    def get_cards(self, list_id: str) -> list:
        path = (
            f'{self.base_url}/lists/{list_id}/cards?'
            f'key={self.api_key}&token={self.token}'
        )

        resp = requests.get(path)
        return resp
