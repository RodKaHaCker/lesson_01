import requests

login = "rodionnewbaltyn@rambler.ru"  # замени на свой логин
password = "Korol_stah1"          # замени на свой пароль

url = "https://yougile.com/api-v2/auth/companies"
payload = {
    "login": login,
    "password": password
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    companies = response.json().get("content", [])
    if companies:
        for company in companies:
            print(f"ID: {company['id']} | Название: {company['name']} | Админ: {company['isAdmin']}")
    else:
        print("У вас нет доступных компаний.")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())
