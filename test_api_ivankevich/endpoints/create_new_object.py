import requests
import allure
from Igor_Vankevich.test_api_ivankevich.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    post_id = None

    @allure.step('Create new object')
    def new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            'https://api.restful-api.dev/objects',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.post_id

    @allure.step('Delete object')
    def delete_object(self):
        post_id = self.response.json()['id']
        yield post_id
        response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
        assert response.status_code == 200


