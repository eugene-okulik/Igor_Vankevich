import requests
import allure
from Igor_Vankevich.test_api_ivankevich.endpoints.endpoint import Endpoint


class ChangeObjectPut(Endpoint):
    @allure.step('PUT change')
    def change_put(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
