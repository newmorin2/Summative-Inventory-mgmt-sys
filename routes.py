from flask import Blueprint, jsonify, request
from data import inventory
from services.openfood import get_product_by_barcode

inventory_routes = Blueprint(
    "inventory_routes",
    __name__
)


@inventory_routes.route("/inventory", methods=["GET"])
def get_inventory():

    return jsonify(inventory), 200


@inventory_routes.route("/inventory/<int:id>", methods=["GET"])
def get_product(id):

    for product in inventory:

        if product["id"] == id:
            return jsonify(product), 200


    return jsonify({
        "message":"Product not found"
    }),404


@inventory_routes.route("/inventory", methods=["POST"])
def create_product():
    data = request.get_json()
    product = {
        "id": len(inventory)+1,
        "name": data["name"],
        "barcode": data["barcode"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(product)
    return jsonify(product),201

@inventory_routes.route("/inventory/<int:id>", methods=["PATCH"])
def update_product(id):
    data = request.get_json()

    for product in inventory:

        if product["id"] == id:
            product.update(data)
            return jsonify(product),200

    return jsonify({
        "message":"Product not found"
    }),404


@inventory_routes.route("/inventory/<int:id>", methods=["DELETE"])
def delete_product(id):

    for product in inventory:

        if product["id"] == id:

            inventory.remove(product)
            return jsonify({
                "message":"Product deleted"
            }),200

    return jsonify({
        "message":"Product not found"
    }),404

@inventory_routes.route("/fetch-product/<barcode>", methods=["GET"])
def fetch_product(barcode):

    product = get_product_by_barcode(barcode)

    if product is None:
        return jsonify({
            "message":"Product not found"
        }),404

    return jsonify(product),200