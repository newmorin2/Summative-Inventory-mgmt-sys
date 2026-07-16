from flask import Flask, jsonify, request
from routes import inventory_routes

app = Flask(__name__)

app.register_blueprint(
    inventory_routes
)



if __name__ == "__main__":
    app.run(debug=True)