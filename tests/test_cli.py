import builtins

import cli


class DummyResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload


def test_view_all_items_prints_inventory(monkeypatch, capsys):
    monkeypatch.setattr(cli.requests, 'get', lambda *args, **kwargs: DummyResponse({'inventory': [{'id': 1, 'name': 'Milk', 'quantity': 2, 'price': 1.5}]}))

    cli.view_all_items()

    captured = capsys.readouterr().out
    assert 'Milk' in captured
    assert '1.5' in captured


def test_update_item_uses_patch_request(monkeypatch, capsys):
    responses = iter([
        DummyResponse({'id': 1, 'name': 'Milk', 'quantity': 2, 'price': 3.99}),
    ])

    monkeypatch.setattr(builtins, 'input', lambda prompt='': '1' if prompt == 'Enter item id: ' else 'price' if prompt == 'Which field do you want to update? (price/quantity): ' else '3.99')
    monkeypatch.setattr(cli.requests, 'patch', lambda *args, **kwargs: next(responses))

    cli.update_item()

    captured = capsys.readouterr().out
    assert 'Item updated successfully.' in captured
    assert '3.99' in captured


def test_import_item_from_external_api(monkeypatch, capsys):
    monkeypatch.setattr(builtins, 'input', lambda prompt='': '1234567890123')
    monkeypatch.setattr(cli.requests, 'post', lambda *args, **kwargs: DummyResponse({'id': 3, 'name': 'Imported Snack', 'brand': 'BrandX', 'barcode': '1234567890123', 'price': 0.0, 'quantity': 1}))

    cli.import_item_from_external_api()

    captured = capsys.readouterr().out
    assert 'Imported item added successfully.' in captured
    assert 'Imported Snack' in captured
