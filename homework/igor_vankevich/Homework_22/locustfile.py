from locust import task, HttpUser
import random


class ListObject(HttpUser):

    @task(1)
    def get_all_obj(self):
        self.client.get('/object')

    @task(4)
    def get_odj(self):
        self.client.get(f'/object/{random.choice([13, 1, 7])}')
