import requests


def create_odj():
    body = {
        "name": "Apple MacBook Pro 16",
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
    ).json()
    assert res['name'] == "Apple MacBook Pro 16"


def new_odj():
    body = {
        "name": "Apple MacBook Pro 16",
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
    return res.json()['id']


def change_obj_put():
    obj_id = new_odj()
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
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body,
        headers=headers
    ).json()
    assert res['name'] == "Apple MacBook Prodwdwdawdaw 16"
    clear(obj_id)


def change_obj_patch():
    obj_id = new_odj()
    body = {
        "name": "Apple MacBook Prodwdwdawdaw 11111116",
        "data": {
            "CPU model": "Intel Core wadwdawdi9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    res = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body,
        headers=headers
    ).json()
    assert res['name'] == "Apple MacBook Prodwdwdawdaw 11111116"
    clear(obj_id)


def clear(obj_id):
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')


def delete_odj():
    obj_id = new_odj()
    res = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    print(res.json())


create_odj()
change_obj_put()
change_obj_patch()
delete_odj()
