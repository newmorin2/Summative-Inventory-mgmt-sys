from unittest.mock import patch

import cli



@patch("cli.requests.get")
def test_view_inventory(mock_get):


    mock_get.return_value.status_code = 200


    mock_get.return_value.json.return_value = [

        {

            "id":1,

            "name":"Laptop",

            "price":1200,

            "stock":5

        }

    ]


    cli.view_inventory()



    mock_get.assert_called_once()