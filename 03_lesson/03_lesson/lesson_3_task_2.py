from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79001234567"),
    Smartphone("Samsung", "Galaxy S24", "+79109876543"),
    Smartphone("Xiaomi", "Mi 14", "+79203334455"),
    Smartphone("Google", "Pixel 8", "+79302223344"),
    Smartphone("OnePlus", "12", "+79401112233")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
