from unittest.mock import patch

from services.openfood import get_product_by_barcode

@patch("services.openfood.requests.get")
def test_barcode_lookup(mock_get):
    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "status":1,
        "product":{
            "product_name":"Coca Cola",
            "brands":"Coca Cola",
            "categories":"Drinks"
        }
    }

    result = get_product_by_barcode(
        "5449000000996"
    )

    assert result["name"] == "Coca Cola"
    assert result["brand"] == "Coca Cola"