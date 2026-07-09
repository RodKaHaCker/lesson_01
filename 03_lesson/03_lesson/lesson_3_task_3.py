from address import Address
from mailing import Mailing

to_address = Address("101000", "Москва", "Тверская", "1", "2")
from_address = Address("190000", "Санкт-Петербург", "Невский", "10", "5")

mail = Mailing(to_address, from_address, 250.50, "TRACK123456")

print(
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей.")
