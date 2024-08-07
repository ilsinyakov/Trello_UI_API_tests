import requests
from allure import step


class CardsApi:
    def __init__(self, base_url: str, api_key: str, token: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.token = token

    @step("Create card by API")
    def create_card(self, list_id: str, card_name: str) -> dict:
        path = (
            f'{self.base_url}/cards/?idList={list_id}'
            f'&key={self.api_key}&token={self.token}'
        )
        body = {
            "name": card_name
        }

        resp = requests.post(path, json=body)
        return resp.json()
