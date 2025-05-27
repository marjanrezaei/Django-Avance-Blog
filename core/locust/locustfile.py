from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    def on_start(self):
        """ on_start is called when a Locust user starts before any task is scheduled """
        response = self.client.post("/accounts/api/v2/jwt/create/", {
            "email": "marjan@gmail.com",
            "password": "123"
        }).json()
        self.client.headers.update({
            "Authorization": f"Bearer {response['access']}"
        })

    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")
        
    @task
    def post_category(self):
        self.client.get("/blog/api/v1/category/")