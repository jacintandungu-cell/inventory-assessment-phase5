from external_api import fetch_product


def test_fetch_product_returns_expected_keys(monkeypatch):
    class DummyResponse:
        status_code = 200

        def json(self):
            return {
                'status': 1,
                'product': {
                    'product_name': 'Sample Product',
                    'brands': 'Sample Brand',
                    'ingredients_text': 'water',
                },
            }

    class DummyRequest:
        def get(self, *args, **kwargs):
            return DummyResponse()

    monkeypatch.setattr('external_api.requests', DummyRequest())

    result = fetch_product('1234567890123')

    assert result['product_name'] == 'Sample Product'
    assert result['brands'] == 'Sample Brand'
    assert result['ingredients_text'] == 'water'
