import requests


class BoardsApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def post_board(self, name: str) -> dict:
        path = f'{self.base_url}/boards'

        header = {
            "Cookie": f"cloud.session.token={self.token}"
        }

        body = {"name": name}

        resp = requests.post(path, json=body, headers=header)
        return resp.json()

    def delete_board(self, board_id: str) -> int:
        path = f'{self.base_url}/boards/{board_id}'

        header = {
            "Cookie": f"cloud.session.token={self.token}"
        }
        resp = requests.delete(path, headers=header)
        return resp.status_code
