import pytest
import init_db

@pytest.fixture
def api(monkeypatch):
    test_dogs = [
        {'id': 1, 'name': 'Test Dog 1', 'age': 7},
        {'id': 2, 'name': 'Test Dog 2', 'age': 4}
    ]
    monkeypatch.setattr(init_db, "db", test_dogs)
    api = init_db.app.test_client()
    return api
