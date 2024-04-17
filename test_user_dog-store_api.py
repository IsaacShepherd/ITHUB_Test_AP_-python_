import requests
import uuid

ENDPOINT = "https://petstore.swagger.io/v2/user"


def test_can_create_user():
    pass


def test_can_get_user_by_username():
    pass


def test_can_update_user():
    pass


def test_can_delete_user():
    pass


def test_can_login_user():
    pass


# helper functions / вспомогательные функции


def new_user_payload():
    return {
        "id": uuid.uuid4(),
        "username": "AllanWake",
        "firstName": "Allan",
        "lastName": "Wake",
        "email": "alanwake@gmail.com",
        "password": "qwerty1",
        "phone": "555555555",
        "userStatus": 0
    }
