from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "name": "Laptop",
        "barcode": "123456",
        "price": 1200,
        "stock": 5
    },
    {
        "id": 2,
        "name": "Mouse",
        "barcode": "789101",
        "price": 25,
        "stock": 50
    }
]


@app.route("/inventory", methods=["GET"])
def get_inventory():

    return jsonify(inventory), 200


@app.route("/inventory/<int:id>", methods=["GET"])
def get_item(id):

    for item in inventory:
        if item["id"] == id:
            return jsonify(item), 200

    return jsonify({
        "message": "Item not found"
    }), 404


@app.route("/inventory", methods=["POST"])
def add_item():

    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "barcode": data["barcode"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_item(id):

    data = request.get_json()

    for item in inventory:

        if item["id"] == id:

            if "name" in data:
                item["name"] = data["name"]

            if "price" in data:
                item["price"] = data["price"]

            if "stock" in data:
                item["stock"] = data["stock"]

            return jsonify(item), 200


    return jsonify({
        "message": "Item not found"
    }), 404


@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):

    for item in inventory:

        if item["id"] == id:

            inventory.remove(item)

            return jsonify({
                "message": "Item deleted"
            }), 200


    return jsonify({
        "message": "Item not found"
    }), 404



if __name__ == "__main__":
    app.run(debug=True)