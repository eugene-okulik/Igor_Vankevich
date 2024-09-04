import requests
import allure
from Igor_Vankevich.test_api_ivankevich.endpoints.endpoint import Endpoint


class ChangeObjectPatch(Endpoint):
    @allure.step('PATCH change')
    def change_patch(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
