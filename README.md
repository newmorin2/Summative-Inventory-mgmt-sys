# Project name
Inventory management system
# Project Description
This system will allow employees to add, edit, view, and delete inventory items. Additionally, the system will fetch real-time product data from an external API (e.g., OpenFoodFacts API) to supplement product details.
# Installation
- git clone <git@github.com:newmorin2/Summative-Inventory-mgmt-sys.git>

- cd ecommerce-admin

- python -m venv venv
- source venv/bin/activate   # Linux/macOS
- venv\Scripts\activate      # Windows

- pip install -r requirements.txt
# Running the API
flask --app app run --debug
# Running the CLI
python cli.py