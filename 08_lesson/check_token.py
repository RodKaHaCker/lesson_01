import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("YOUGILE_TOKEN")

print("Токен из .env:", token)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

url = "https://yougile.com/api-v2/projects"

response = requests.get(url, headers=headers)

print(f"Статус: {response.status_code}")
print("Ответ:", response.json())
