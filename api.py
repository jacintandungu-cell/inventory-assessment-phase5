import requests


def fetch_product_by_barcode(barcode):
    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
    except requests.RequestException:
        return None

    if data.get('status') != 1:
        return None

    product = data.get('product', {})
    return {
        'product_name': product.get('product_name'),
        'brands': product.get('brands'),
        'ingredients_text': product.get('ingredients_text'),
    }
