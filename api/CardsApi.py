import requests
from allure import step


class CardsApi:
    def __init__(self, base_url: str, api_key: str, token: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.token = token

    @step('Create card by API')
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

    @step('Delete card by API')
    def delete_card(self, card_id: str) -> int:
        path = (
            f'{self.base_url}/cards/{card_id}?'
            f'&key={self.api_key}&token={self.token}'
        )
        resp = requests.delete(path)
        return resp.status_code

    @step('Get card info by API')
    def get_card(self, card_id: str) -> dict:
        path = (
            f'{self.base_url}/cards/{card_id}?'
            f'&key={self.api_key}&token={self.token}'
        )
        resp = requests.get(path)
        return resp.json()

    def is_card_list_updated(self, card_id: str, new_list_id: str) -> bool:
        list_id = self.get_card(card_id)["idList"]
        if list_id == new_list_id:
            return True
        else:
            return False

    def is_card_name_updated(self, card_id: str, new_card_name: str) -> bool:
        card_name = self.get_card(card_id)["name"]
        if card_name == new_card_name:
            return True
        else:
            return False

    @step('Update card name by API')
    def update_card_name(self, card_id: str, new_card_name: str) -> dict:
        path = (
            f'{self.base_url}/cards/{card_id}?'
            f'&key={self.api_key}&token={self.token}'
        )
        body = {
            "name": new_card_name
        }

        resp = requests.put(path, json=body)
        return resp.json()

    @step('Update card column by API')
    def update_card_list(self, card_id: str, new_list_id: str) -> dict:
        path = (
            f'{self.base_url}/cards/{card_id}?'
            f'&key={self.api_key}&token={self.token}'
        )
        body = {
            "idList": new_list_id
        }

        resp = requests.put(path, json=body)
        return resp.json()
