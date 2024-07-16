import configparser


config = configparser.ConfigParser()
config.sections()
config.read('test_config.ini')


class ConfigProvider:
    def __init__(self) -> None:
        pass

    def get(self, section: str, prop: str):
        return config[section][prop]
