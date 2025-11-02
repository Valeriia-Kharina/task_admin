# load_test.py
from locust import HttpUser, task, between
import uuid
import random

class TaskAppUser(HttpUser):
    wait_time = between(1, 3)  # паузи між діями у секундах

    def on_start(self):
        self.client.post("/reset")
        pass

    @task(4)
    def view_tasks(self):
        self.client.get("/tasks", name="/tasks [GET]")

    @task(3)
    def add_task(self):
        name = f"task-{uuid.uuid4().hex[:8]}"
        self.client.post("/tasks", json={"name": name}, name="/tasks [POST]")

    @task(2)
    def update_status(self):
        r = self.client.get("/tasks")
        if r.status_code == 200:
            items = r.json()
            if items:
                t = random.choice(items)
                self.client.put("/tasks/status", json={"name": t['name'], "status": "Done"}, name="/tasks/status [PUT]")

    @task(1)
    def delete_task(self):
        r = self.client.get("/tasks")
        if r.status_code == 200:
            items = r.json()
            if items:
                t = random.choice(items)
                self.client.delete("/tasks", json={"name": t['name']}, name="/tasks [DELETE]")
