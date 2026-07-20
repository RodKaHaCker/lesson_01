import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ProjectAPI:
    BASE_URL = "https://yougile.com/api-v2"
    TOKEN = os.getenv("YOUGILE_TOKEN")

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.TOKEN}"
        }

    def create_project(self, title, users=None):
        url = f"{self.BASE_URL}/projects"
        data = {"title": title}
        if users:
            data["users"] = users
        return requests.post(url, json=data, headers=self.headers)

    def update_project(self, project_id, title, users=None):
        url = f"{self.BASE_URL}/projects/{project_id}"
        data = {"title": title}
        if users:
            data["users"] = users
        return requests.put(url, json=data, headers=self.headers)

    def get_project(self, project_id):
        url = f"{self.BASE_URL}/projects/{project_id}"
        return requests.get(url, headers=self.headers)
