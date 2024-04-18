import requests
import uuid

ENDPOINT = "https://petstore.swagger.io/v2/user"


def test_can_create_user():
    payload = new_user_payload()
    user_name = payload["username"]
    delete_user(user_name)
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 200

    data = create_user_response.json()

    get_user_response = get_user_by_user_name(user_name)

    assert get_user_response.status_code == 200
    get_user_data = get_user_response.json()
    assert get_user_data["id"] == int(data["message"])


def test_can_get_user_by_user_name():
    payload = new_user_payload()
    user_name = payload["username"]
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 200

    get_user_response = get_user_by_user_name(user_name)

    assert get_user_response.status_code == 200


def test_can_update_user_first_name():
    payload = new_user_payload()
    user_name = payload["username"]
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 200

    new_payload = {
        "id": payload["id"],
        "username": payload["username"],
        "firstName": "Vovchik",
        "lastName": payload["lastName"],
        "email": payload["email"],
        "password": payload["password"],
        "phone": payload["phone"],
        "userStatus": payload["userStatus"]
    }
    update_user_response = update_user(user_name, new_payload)
    assert update_user_response.status_code == 200

    get_user_response = get_user_by_user_name(user_name)
    assert get_user_response.status_code == 200

    get_user_data = get_user_response.json()
    assert get_user_data["firstName"] == new_payload["firstName"]


def test_can_delete_user():
    payload = new_user_payload()
    user_name = payload["username"]
    delete_user(user_name)
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 200

    delete_user_response = delete_user(user_name)
    assert delete_user_response.status_code == 200

    get_user_response = get_user_by_user_name(user_name)
    assert get_user_response.status_code == 404


def test_can_login_user():
    payload = new_user_payload()
    user_name = payload["username"]
    password = payload["password"]
    create_user_response = create_user(payload)
    assert create_user_response.status_code == 200

    login_user_response = login_user(user_name, password)
    assert login_user_response.status_code == 200


# helper functions / вспомогательные функции


def new_user_payload():
    return {
        "id": 888,
        "username": "AllanWake",
        "firstName": "Allan",
        "lastName": "Wake",
        "email": "alanwake@gmail.com",
        "password": "qwerty1",
        "phone": "555555555",
        "userStatus": 0
    }


def create_user(payload):
    return requests.post(ENDPOINT, json=payload)


def get_user_by_user_name(user_name):
    return requests.get(ENDPOINT + f"/{user_name}")


def update_user(user_name, payload):
    return requests.put(ENDPOINT + f"/{user_name}", json=payload)


def delete_user(user_name):
    return requests.delete(ENDPOINT + f"/{user_name}")


def login_user(login, password):
    return requests.get(ENDPOINT + f"/login?username={login}&password={password}")
