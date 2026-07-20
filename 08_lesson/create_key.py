import requests

login = "rodionnewbaltyn@rambler.ru"
password = "Korol_stah1"
company_id = "98f71e2b-0dde-4f96-bc09-030ea3bcc20b"

url = "https://yougile.com/api-v2/auth/keys"
payload = {
    "login": login,
    "password": password,
    "companyId": company_id
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    api_key = response.json().get("key")
    print(f"API-ключ: {api_key}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())
