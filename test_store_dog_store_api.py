import requests
from test_pet_dog_store_api import new_pet_payload
from test_pet_dog_store_api import create_pet


ENDPOINT = "https://petstore.swagger.io/v2/store"


def test_can_get_store_inventory():
    inventory_response = get_store_inventory()
    data = inventory_response.json()
    # print(data)
    assert inventory_response.status_code == 200


def test_can_create_order():
    new_pet = new_pet_payload()
    create_pet_response = create_pet(new_pet)
    assert create_pet_response.status_code == 200

    payload = new_order_payload()
    create_order_response = create_order(payload)
    assert create_order_response.status_code == 200

    data = create_order_response.json()
    order_id = data["id"]
    get_order_response = get_order_byID(order_id)

    assert get_order_response.status_code == 200
    get_order_data = get_order_response.json()
    assert get_order_data["petId"] == payload["petId"]
    assert get_order_data["id"] == payload["id"]


def test_can_get_order_by_id():
    new_pet = new_pet_payload()
    create_pet_response = create_pet(new_pet)
    assert create_pet_response.status_code == 200

    payload = new_order_payload()
    create_order_response = create_order(payload)
    assert create_order_response.status_code == 200

    data = create_order_response.json()
    order_id = data["id"]
    get_order_response = get_order_byID(order_id)

    assert get_order_response.status_code == 200


def test_can_delete_order():
    new_pet = new_pet_payload()
    create_pet_response = create_pet(new_pet)
    assert create_pet_response.status_code == 200

    payload = new_order_payload()
    create_order_response = create_order(payload)
    assert create_order_response.status_code == 200

    data = create_order_response.json()
    order_id = data["id"]
    delete_order_by_id(order_id)
    delete_order_response = get_order_byID(order_id)
    assert delete_order_response.status_code == 404


def test_cannot_delete_order_if_not_exist():
    new_pet = new_pet_payload()
    create_pet_response = create_pet(new_pet)
    assert create_pet_response.status_code == 200

    payload = new_order_payload()
    create_order_response = create_order(payload)
    assert create_order_response.status_code == 200

    data = create_order_response.json()
    order_id = data["id"]
    delete_order_by_id(order_id)
    delete_order_response = get_order_byID(order_id)
    assert delete_order_response.status_code == 404

    delete_order_by_id(order_id)
    assert delete_order_response.status_code == 404


# helper functions / вспомогательные функции


def get_store_inventory():
    return requests.get(ENDPOINT + "/inventory")


def create_order(payload):
    return requests.post(ENDPOINT + "/order", json=payload)


def get_order_byID(order_id):
    return requests.get(ENDPOINT + f"/order/{order_id}")


def delete_order_by_id(order_id):
    return requests.delete(ENDPOINT + f"/order/{order_id}")


def new_order_payload():
    return {
        "id": 5,
        "petId": 6,
        "quantity": 1,
        "shipDate": "2024-04-13T15:55:15.644Z",
        "status": "placed",
        "complete": True
    }
