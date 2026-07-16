import pytest

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200

def test_get_single_product(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200
    data = response.get_json()

    assert data["name"] == "Laptop"

def test_create_product(client):
    new_product = {
        "name":"Keyboard",
        "barcode":"99999",
        "price":50,
        "stock":10
    }

    response = client.post(
        "/inventory",
        json=new_product

    )
    assert response.status_code == 201

def test_update_product(client):
    response = client.patch(
        "/inventory/1",
        json={

            "price":1500
        }
    )
    assert response.status_code == 200


def test_delete_product(client):

    response = client.delete(
        "/inventory/2"
    )
    assert response.status_code == 200