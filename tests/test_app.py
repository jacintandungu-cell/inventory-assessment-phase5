import app as app_module


def test_get_inventory_returns_inventory_list():
    client = app_module.app.test_client()

    response = client.get('/inventory')

    assert response.status_code == 200
    assert response.get_json()['inventory'][0]['name'] == 'Organic Almond Milk'


def test_create_inventory_item_returns_created_item():
    client = app_module.app.test_client()
    payload = {
        'name': 'Test Yogurt',
        'brand': 'Acme',
        'barcode': '1111111111111',
        'price': 4.5,
        'quantity': 7,
    }

    response = client.post('/inventory', json=payload)

    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == payload['name']
    assert data['brand'] == payload['brand']
    assert data['barcode'] == payload['barcode']


def test_update_inventory_item_changes_requested_field():
    client = app_module.app.test_client()

    response = client.patch('/inventory/1', json={'quantity': 15})

    assert response.status_code == 200
    assert response.get_json()['quantity'] == 15


def test_import_inventory_from_external_api_adds_item(monkeypatch):
    client = app_module.app.test_client()

    def fake_fetch_product(barcode):
        return {'product_name': 'Imported Snack', 'brands': 'BrandX', 'ingredients_text': 'salt'}

    monkeypatch.setattr(app_module, 'fetch_product', fake_fetch_product)

    response = client.post('/inventory/import/1234567890123')

    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Imported Snack'
    assert data['brand'] == 'BrandX'
    assert data['barcode'] == '1234567890123'
