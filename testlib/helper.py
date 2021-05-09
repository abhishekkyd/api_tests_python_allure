import allure
import config
from requests import Request
from . import http_session
# from waiting import wait
from config.routing import BASE_URL


# COMMON
def check_and_return_json(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        response.raise_for_status()
        return response.json()
    return wrapper


def check_and_return_text(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        response.raise_for_status()
        return response.text
    return wrapper


def send_request_and_get_response(func):
    def wrapper(by_user='authorized', *args, **kwargs):
        request = func(*args, **kwargs)
        with allure.step(f"Send {request.method} request by {by_user} user to url:\n {request.url}"):
            response = http_session.send_request(request=request, by_user=by_user)
            return response
    return wrapper


def get_user_id_from_response(response):
    json = response.json()
    user_id = get_user_id_from_json(json)
    return user_id


def get_user_id_from_json(json):
    user_id = json.get('id')
    return user_id


@send_request_and_get_response
def get_request(url, **kwargs):
    return Request(method='GET', url=BASE_URL + url, **kwargs)


@send_request_and_get_response
def post_request(url, body, **kwargs):
    return Request(method='POST', url=BASE_URL + url,
                   params=body,
                   headers={'Content-Type':'application/json',
                            'Authorization': 'Bearer {}'.format(config.auth.EXPIRED_TOKEN)},
                   **kwargs)


@send_request_and_get_response
def put_request(url, body, **kwargs):
    return Request(method='PUT', url=BASE_URL + url,
                   params=body,
                   headers={'Content-Type':'application/json',
                            'Authorization': 'Bearer {}'.format(config.auth.EXPIRED_TOKEN)},
                   **kwargs)


@send_request_and_get_response
def delete_request(url, **kwargs):
    return Request(method='DELETE', url=BASE_URL + url,
                   headers={'Content-Type':'application/json',
                            'Authorization': 'Bearer {}'.format(config.auth.EXPIRED_TOKEN)},
                   **kwargs)
