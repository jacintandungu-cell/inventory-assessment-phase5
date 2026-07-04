# Inventory Management API

A Flask-based inventory management system for tracking products, adding new items, updating stock, and importing product information from the OpenFoodFacts API by barcode.

## Features

- View all inventory items
- View a single inventory item
- Create a new inventory item
- Update an existing inventory item
- Delete an inventory item
- Import a product from the external API by barcode
- Use a simple CLI to interact with the inventory API

## Technologies

- Python
- Flask
- Requests
- Pipenv
- Pytest

## Installation

1. Clone the repository.
2. Install dependencies with Pipenv:

```bash
pipenv install
```

## Running the API

Start the Flask server:

```bash
pipenv run python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

- GET /inventory - View all inventory items
- GET /inventory/<item_id> - View one inventory item
- POST /inventory - Create a new inventory item
- PATCH /inventory/<item_id> - Update an item
- DELETE /inventory/<item_id> - Delete an item
- POST /inventory/import/<barcode> - Import an item from the external API

## Running the CLI

```bash
pipenv run python cli.py
```

## Running Tests

```bash
pipenv run pytest -q
```

## Notes

The current implementation stores inventory in memory using the data module.
