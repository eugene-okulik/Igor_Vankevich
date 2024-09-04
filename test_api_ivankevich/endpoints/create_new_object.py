import requests
import allure
from Igor_Vankevich.test_api_ivankevich.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    post_id = None

    @allure.step('Create new object')
    def new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        print(f'\nObject created: {self.post_id}')
        return self.response
