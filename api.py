import requests


HEADERS = {
    'User-Agent': 'InventoryManagementSystem/1.0 (https://github.com/jacintandungu-cell/inventory-assessment-phase5)',
}


def fetch_product_by_barcode(barcode):
    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        data = response.json()
    except requests.RequestException:
        return None

    if response.status_code != 200 or data.get('status') != 1:
        return None

    product = data.get('product', {})
    return {
        'product_name': product.get('product_name'),
        'brands': product.get('brands'),
        'ingredients_text': product.get('ingredients_text'),
    }
