import requests
import uuid

ENDPOINT = "https://petstore.swagger.io/v2/user"


def test_can_create_user():
    new_user = new_user_payload()
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 200

    data = create_user_response.json()

    user_id = data["id"]
    user_name = data["name"]
    get_user_response = get_user_by_user_name(user_name)

    assert get_user_response.status_code == 200
    get_user_data = get_user_response.json()
    assert get_user_data["name"] == payload["name"]
    assert get_user_data["id"] == payload["id"]


def test_can_get_user_by_user_name():
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
        "id": uuid.uuid4().int,
        "username": "AllanWake",
        "firstName": "Allan",
        "lastName": "Wake",
        "email": "alanwake@gmail.com",
        "password": "qwerty1",
        "phone": "555555555",
        "userStatus": 0
    }

def create_user(payload):
    return requests.post(ENDPOINT, json = payload)


def get_user_by_user_name(user_name):
    return requests.get(ENDPOINT + f"/{user_name}")