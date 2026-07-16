import requests

def get_product_by_barcode(barcode):

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None

    product = data["product"]

    return {
        "name": product.get("product_name"),
        "brand": product.get("brands"),
        "category": product.get("categories")
    }