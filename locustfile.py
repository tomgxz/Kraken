from locust import HttpUser, task

class KrakenLoadUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/login")
        self.client.get("/signup")
        self.client.get("/home")