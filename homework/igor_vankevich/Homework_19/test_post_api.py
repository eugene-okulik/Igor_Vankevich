import pytest
import requests


@pytest.fixture(scope='session')
def process_testing():
    print('Start testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='function')
def process_test():
    print('before test')
    yield
    print('\nafter test')


@pytest.mark.parametrize('name', ['mcbook', 'notPC', 'bla?*(?№;*:bla'])
def test_create_object(name, process_testing, process_test):
    body = {
        "name": name,
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    res = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    assert res.status_code == 200


@pytest.fixture()
def object_id(process_test):
    body = {
        "name": 'macbook1212',
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    res = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    post_id = res.json()['id']
    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.mark.critical
def test_change_obj_put(object_id, process_test):
    body = {
        "name": "Apple MacBook Prodwdwdawdaw 16",
        "data": {
            "year": 20134239,
            "price": 18492323.99,
            "CPU model": "Intel Core wadwdawdi9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    res = requests.put(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=body,
        headers=headers
    )
    assert res.json()['name'] == "Apple MacBook Prodwdwdawdaw 16"


@pytest.mark.medium
def test_change_obj_patch(object_id, process_test):
    body = {
        "name": "Apple MacBook Prodwdwdawdaw 11111116",
        "data": {
            "CPU model": "Intel Core wadwdawdi9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    res = requests.put(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=body,
        headers=headers
    )
    assert res.json()['name'] == "Apple MacBook Prodwdwdawdaw 11111116"


def test_delete_odj(object_id, process_test):
    res = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    assert res.status_code == 200
