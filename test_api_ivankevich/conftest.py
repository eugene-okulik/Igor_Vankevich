import pytest
from endpoints.create_new_object import CreateObject
from endpoints.change_object_put import ChangeObjectPut
from endpoints.change_object_patch import ChangeObjectPatch
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_new_object():
    return CreateObject()


@pytest.fixture()
def post_id(create_new_object, delete_object):
    body = {"name": 'mc1',
            "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
    create_new_object.new_object(body)
    yield create_new_object.post_id
    delete_object.delete_object(create_new_object.post_id)


@pytest.fixture()
def change_put_object():
    return ChangeObjectPut()


@pytest.fixture()
def change_patch_object():
    return ChangeObjectPatch()


@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture(scope='session')
def process_testing():
    print('Start testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='function')
def process_test():
    print('before test')
    yield
    print('after test')
