import allure
from allure import severity_level
from allure import step


@allure.feature('Board')
@allure.severity(severity_level.BLOCKER)
@allure.title('Test create board by API')
def test_create_board(board_api_client):
    board_name = 'Created board'
    board_api_client.create_board(board_name)

    with step('Check that created board is present in boards list'):
        assert board_api_client.is_board_in_list(board_name), \
            'Created board is not present in boards list'
