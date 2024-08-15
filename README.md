# Trello UI and API automated tests

## Structure

- ./test - tests
- ./test/test_ui.py - UI tests
- ./test/test_api.py - API tests
- ./test_data.json - test data (logins, passwords, keys, tokens e.g.) - gitignored file!!! You must add this file to root of project
- ./test_config.ini - test configuration (URLs, parameters e.g.)
- ./requirements.txt - python requirements
- ./pytest.ini - pytest options
- ./DataProvider.py - test data provider
- ./ConfigProvider.py - configuration provider
- ./api - API classes for API tests
- ./pages - pages classes for UI tests

## Install Requirements

`pip install -r requirements.txt`

## Run UI tests

`pytest test/test_ui.py`

## Run API tests

`pytest test/test_api.py`

## Run all of tests

`pytest`

## Allure report

### Generate allure web-report

`allure serve allure-files`