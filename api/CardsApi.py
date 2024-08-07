# import requests
# from allure import step


class CardsApi:
    def __init__(self, base_url: str, api_key: str, token: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.token = token

    # def get_card_list(self, )
