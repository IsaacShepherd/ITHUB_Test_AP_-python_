import requests

ENDPOINT = "https://petstore.swagger.io/v2"


def test_can_get_pet_byID():
    pet_ID = 5
    response = get_pet_byID(pet_ID)
    assert response.status_code == 200


def test_can_create_pet():
    payload = new_pet_payload()
    create_pet_response = create_pet(payload)
    assert create_pet_response.status_code == 200

    data = create_pet_response.json()

    pet_id = data["id"]
    get_pet_response = get_pet_byID(pet_id)

    assert get_pet_response.status_code == 200
    get_pet_data = get_pet_response.json()
    assert get_pet_data["name"] == payload["name"]
    assert get_pet_data["id"] == payload["id"]


def test_can_update_pet_name():
    payload = new_pet_payload()
    create_pet_response = create_pet(payload)
    pet_id = create_pet_response.json()["id"]

    new_payload = {
        "id": pet_id,
        "category": payload["category"],
        "name": "rex",
        "photoUrls": payload["photoUrls"],
        "tags": payload["tags"],
        "status": payload["status"]
    }
    update_pet_response = update_pet(new_payload)
    assert update_pet_response.status_code == 200

    get_pet_response = get_pet_byID(pet_id)
    assert get_pet_response.status_code == 200

    get_pet_data = get_pet_response.json()
    assert get_pet_data["name"] == new_payload["name"]


def test_can_update_pet_status():
    payload = new_pet_payload()
    create_pet_response = create_pet(payload)
    pet_id = create_pet_response.json()["id"]

    new_payload = {
        "id": pet_id,
        "category": payload["category"],
        "name": payload["name"],
        "photoUrls": payload["photoUrls"],
        "tags": payload["tags"],
        "status": "sold"
    }
    update_pet_response = update_pet(new_payload)
    assert update_pet_response.status_code == 200

    get_pet_response = get_pet_byID(pet_id)
    assert get_pet_response.status_code == 200

    get_pet_data = get_pet_response.json()
    assert get_pet_data["status"] == new_payload["status"]


def test_can_delete_pet():
    payload = new_pet_payload()
    create_pet_response = create_pet(payload)
    pet_id = create_pet_response.json()["id"]

    delete_pet(pet_id)
    get_pet_response = get_pet_byID(pet_id)
    assert get_pet_response.status_code == 404


# helper functions / вспомогательные функции

def create_pet(payload):
    return requests.post(ENDPOINT + "/pet", json=payload)


def update_pet(payload):
    return requests.put(ENDPOINT + "/pet", json=payload)


def get_pet_byID(pet_id):
    return requests.get(ENDPOINT + f"/pet/{pet_id}")


def new_pet_payload():
    return {
        "id": 6,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "barbos",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }


def delete_pet(pet_id):
    return requests.delete(ENDPOINT + f"/pet/{pet_id}")
