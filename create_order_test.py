#Людмила Нижегородова, 8а-когорта, Финальный проект, Инженер по тестированию плюс
import sender_stand_request
import data


def test_create_order_exist():
    order_response = sender_stand_request.post_new_order(data.order_body)
    assert order_response.status_code == 201
    assert order_response.json()['track'] != ''

    current_track = order_response.json()['track']
    order_exist_response = sender_stand_request.get_order_exist(current_track)
    assert order_exist_response.status_code == 200
