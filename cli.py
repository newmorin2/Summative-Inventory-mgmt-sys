import requests
BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(
        f"{BASE_URL}/inventory"
    )

    if response.status_code == 200:

        products = response.json()

        for product in products:

            print("----------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Stock:", product["stock"])

    else:
        print("Could not fetch inventory")

def add_product():
    name = input("Product name: ")
    barcode = input("Barcode: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))


    product = {
        "name": name,
        "barcode": barcode,
        "price": price,
        "stock": stock

    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=product
    )

    if response.status_code == 201:
        print("Product added successfully")

    else:
        print("Failed to add product")


def update_product():
    product_id = input("Product ID: ")
    price = input("New price: ")
    stock = input("New stock: ")
    data = {}

    if price:
        data["price"] = float(price)

    if stock:
        data["stock"] = int(stock)

    response = requests.patch(
        f"{BASE_URL}/inventory/{product_id}",
        json=data

    )

    if response.status_code == 200:
        print("Updated successfully")

    else:
        print("Product not found")


def delete_product():
    product_id = input("Product ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{product_id}"
    )
    if response.status_code == 200:
        print("Deleted successfully")

    else:
        print("Product not found")


def find_product():

    barcode = input("Enter barcode: ")
    response = requests.get(

        f"{BASE_URL}/fetch-product/{barcode}"

    )

    if response.status_code == 200:

        product = response.json()

        print("\nProduct Found")
        print("----------------")
        print("Name:", product["name"])
        print("Brand:", product["brand"])
        print("Category:", product["category"])

    else:
        print("Product not found")


def menu():
    while True:
        print("\n====== INVENTORY ADMIN ======")

        print("1. View Inventory")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Find Product")
        print("6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_product()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            find_product()

        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()