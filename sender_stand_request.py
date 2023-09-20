import conf
import requests
# import data


def post_new_order(body):
    return requests.post(conf.URL_SERVICE + conf.ORDER_CREATE_PATH,
                         json=body
                         )


def get_order_exist(track):
    current_path = conf.URL_SERVICE + conf.GET_ORDER_PATH + f'?t={track}'
    return requests.get(current_path)
