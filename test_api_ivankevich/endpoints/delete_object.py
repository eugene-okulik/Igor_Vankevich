import requests
import allure
from Igor_Vankevich.test_api_ivankevich.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object')
    def delete_object(self, post_id):
        self.response = requests.delete(f'{self.url}/{post_id}')
        print(f'\nObject {post_id} deleted with status code: {self.response.status_code}')
