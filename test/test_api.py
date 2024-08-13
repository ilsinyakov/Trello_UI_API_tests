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

    with step('Check that created card is in the list'):
        assert list_api_client.is_card_in_list(list_id, card_id), \
            'Created card is not in the list'

    status_code = board_api_client.delete_board_by_name(board_name)
    with step('Check that the created board has been deleted'):
        assert status_code == 200, 'The created board has not been deleted'


@allure.feature('Card')
@allure.severity(severity_level.CRITICAL)
@allure.title('Test update card by API')
def test_update_card(board_api_client, card_api_client):
    board_name = 'Board to update card'
    card_name = 'Test card 6666'
    new_card_name = 'Updated card name'
    board_id = board_api_client.create_board(board_name)["id"]
    list_id = board_api_client.get_lists_on_board(board_id)[0]["id"]
    card_id = card_api_client.create_card(list_id, card_name)["id"]

    card_api_client.update_card_name(card_id, new_card_name)

    with step('Check updated card name'):
        assert card_api_client.is_card_name_updated(card_id, new_card_name), \
            'Card name has not been updated'

    status_code = board_api_client.delete_board_by_name(board_name)
    with step('Check that the created board has been deleted'):
        assert status_code == 200, 'The created board has not been deleted'


@allure.feature('Card')
@allure.severity(severity_level.CRITICAL)
@allure.title('Test delete card by API')
def test_delete_card(board_api_client, card_api_client, list_api_client):
    board_name = 'Board to delete card'
    card_name = 'Test card to delete'

    board_id = board_api_client.create_board(board_name)["id"]
    list_id = board_api_client.get_lists_on_board(board_id)[0]["id"]
    card_id = card_api_client.create_card(list_id, card_name)["id"]

    status_code = card_api_client.delete_card(card_id)
    with step('Check that the card has been deleted'):
        assert status_code == 200, 'The card has not been deleted'
        assert not list_api_client.is_card_in_list(list_id, card_id), \
            "There is deleted card in the list"

    status_code = board_api_client.delete_board_by_name(board_name)
    with step('Check that the created board has been deleted'):
        assert status_code == 200, 'The created board has not been deleted'


@allure.feature('Card')
@allure.severity(severity_level.CRITICAL)
@allure.title('Test move card by API')
def test_move_card(board_api_client, card_api_client):
    board_name = 'Board to move card'
    card_name = 'Test card to move'
    old_list_num = 0  # number of list to which we will create the card
    new_list_num = 1  # number of list to which we will move the card

    board_id = board_api_client.create_board(board_name)["id"]
    list_id = board_api_client.get_lists_on_board(board_id)[old_list_num]["id"]
    new_list_id = board_api_client.\
        get_lists_on_board(board_id)[new_list_num]["id"]
    card_id = card_api_client.create_card(list_id, card_name)["id"]

    card_api_client.update_card_list(card_id, new_list_id)

    with step('Check updated card column'):
        assert card_api_client.is_card_list_updated(card_id, new_list_id), \
            'Card column has not been updated'

    status_code = board_api_client.delete_board_by_name(board_name)
    with step('Check that the created board has been deleted'):
        assert status_code == 200, 'The created board has not been deleted'
