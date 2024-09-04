import pytest

data = [
    {"name": 'mc1', "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": 'mc1', "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": 'mc1', "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
]


@pytest.mark.parametrize('body', data)
def test_create_object(create_new_object, body, process_testing, process_test):
    create_new_object.new_object(body)
    create_new_object.check_response_title_is_correct(body['name'])
    create_new_object.check_that_status_is_200()


def test_object_id(create_new_object, process_test, process_testing):
    body = {
        "name": 'macbook1212',
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_new_object.new_object(body)
    create_new_object.check_response_title_is_correct(body['name'])
    create_new_object.check_that_status_is_200()


def test_change_obj_put(change_put_object, process_test, post_id):
    body = {
        "name": "Apple MacBook Prodwdwdawdaw 16",
        "data": {
            "year": 20134239,
            "price": 18492323.99,
            "CPU model": "Intel Core wadwdawdi9",
            "Hard disk size": "1 TB"
        }
    }
    change_put_object.change_put(post_id, body)
    change_put_object.check_response_title_is_correct(body['name'])
    change_put_object.check_that_status_is_200()


def test_change_obj_patch(change_patch_object, process_test, post_id):
    body = {
        "name": "Apple MacBook Prodwdwdawdaw 16",
        "data": {
            "year": 20134239,
            "price": 18492323.99,
        }
    }
    change_patch_object.change_patch(post_id, body)
    change_patch_object.check_response_title_is_correct(body['name'])
    change_patch_object.check_that_status_is_200()


def test_delete_object(delete_object, process_test, post_id):
    delete_object.delete_object(post_id)
    delete_object.check_that_status_is_200()
