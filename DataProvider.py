import json


test_data_file = open('test_data.json')

test_data = json.load(test_data_file)


class DataProvider():
    def __init__(self) -> None:
        self.data = test_data

    def get(self, prop: str) -> str:
        return self.data.get(prop)
