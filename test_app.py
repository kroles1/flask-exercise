import json
from os import environ

def test_welcome(api):
    res = api.get('/')
    assert res.status == '200 OK'
    assert res.json['message'] == 'Hello from Flask!'

def test_handle_404(api):
    res = api.get('/api/dogs/4')
    assert res.status == '404 NOT FOUND'
    assert 'Not found 404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.' in res.json['message']

def test_get_dogs_error(api):
        res = api.get('/dogs/44')
        assert res.status == '400 BAD REQUEST'

def test_get_dogs(api):
    res = api.get('/dogs')
    # assert res.json == [{"id": 1, "name": "Test1", "age": 7},
    #     {"id": 2, "name": "Test2", "age": 4}]
    # assert len(res.json) == 2
    assert res.status == '200 OK'

# def test_get_dog(api):
#     res = api.get('/dogs/1')
#     assert res.status == '302 FOUND'
#     assert res.json['name'] == 'Test1'

# def test_delete_dog(api):
#     res = api.delete('/dogs/1')
#     assert res.status == '204 NO CONTENT'

def test_post_dogs(api):
    mock_data = json.dumps({"name": "Molly", "age": 5})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/dogs', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'

# def test_patch_dog(api):
#         mock_data = json.dumps({'name': 'Molly'})
#         mock_headers = {'Content-Type': 'application/json'}
#         res = api.patch('/dogs/2', data=mock_data, headers=mock_headers)
#         assert res.json['id'] == 2
#         assert res.json['name'] == 'Molly'
