from flask import Flask, jsonify

from data import inventory

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the inventory management API'})

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify({'inventory': inventory}), 200

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    for item in inventory:
        if item['id'] == item_id:
            return jsonify(item), 200
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
