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

    status_code = board_api_client.delete_board_by_name(board_name)
    with step('Check that the created board has been deleted'):
        assert status_code == 200, 'The created board has not been deleted'


@allure.feature('Board')
@allure.severity(severity_level.CRITICAL)
@allure.title('Test delete board by API')
def test_delete_board(board_api_client):
    board_name = 'Board to delete'
    board_id = board_api_client.create_board(board_name)["id"]

    board_api_client.delete_board_by_id(board_id)

    with step('Check that deleted board is not present in boards list'):
        assert not board_api_client.is_board_in_list(board_name), \
            'Deleted board is present in boards list'


@allure.feature('Card')
@allure.severity(severity_level.BLOCKER)
@allure.title('Test create card by API')
def test_create_card(board_api_client, card_api_client, list_api_client):
    board_name = 'Board to create card'
    card_name = 'Test card 5555'
    board_id = board_api_client.create_board(board_name)["id"]
    list_id = board_api_client.get_lists_on_board(board_id)[0]["id"]

    card_id = card_api_client.create_card(list_id, card_name)["id"]
    
    
