from flask import Flask, jsonify, request

from data import inventory

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the inventory management API'})

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify({'inventory': inventory}), 200

@app.route('/inventory', methods=['POST'])
def create_inventory_item():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    name = data.get('name')
    brand = data.get('brand')
    barcode = data.get('barcode')
    price = data.get('price')
    quantity = data.get('quantity')

    if not name or not brand or not barcode or price is None or quantity is None:
        return jsonify({'error': 'Missing required fields: name, brand, barcode, price, quantity'}), 400

    next_id = inventory[-1]['id'] + 1 if inventory else 1
    new_item = {
        'id': next_id,
        'name': name,
        'brand': brand,
        'barcode': barcode,
        'price': price,
        'quantity': quantity,
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    for item in inventory:
        if item['id'] == item_id:
            return jsonify(item), 200
    return jsonify({'error': 'Item not found'}), 404

@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_inventory_item(item_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    for item in inventory:
        if item['id'] == item_id:
            item.update(data)
            return jsonify(item), 200

    return jsonify({'error': 'Item not found'}), 404

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    for item in inventory:
        if item['id'] == item_id:
            inventory.remove(item)
            return jsonify({'message': 'Item deleted successfully'}), 200
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
