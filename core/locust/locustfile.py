from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")
        
    @task
    def post_category(self):
        self.client.get("/blog/api/v1/category/")