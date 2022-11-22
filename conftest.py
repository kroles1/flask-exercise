import pytest
import app

@pytest.fixture
def api(monkeypatch):
    test_dogs = [
        {'id': 1, 'name': 'Test Dog 1', 'age': 7},
        {'id': 2, 'name': 'Test Dog 2', 'age': 4}
    ]
    monkeypatch.setattr(app, "dogs", test_dogs)
    api = app.app.test_client()
    return api
