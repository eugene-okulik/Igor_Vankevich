import pytest
from endpoints.create_new_object import CreateObject
from endpoints.change_object_put import ChangeObjectPut
from endpoints.change_object_patch import ChangeObjectPatch
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_new_object():
    return CreateObject()


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
    print('\nafter test')
