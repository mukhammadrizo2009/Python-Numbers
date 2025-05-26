from decimal import Decimal, ROUND_HALF_UP
from num2words import num2words


kwh_uchun = Decimal("0.45")


Boshida = Decimal(input("Oy boshidagi ko‘rsatkichni kiriting (kWh): "))
Ohirida = Decimal(input("Oy oxiridagi ko‘rsatkichni kiriting (kWh): "))


ishlatilgan = Ohirida - Boshida


tolov = ishlatilgan * kwh_uchun


tolov = tolov.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


print(f"\nTo‘lov: ${tolov}")
print("In English:", num2words(tolov, lang='en').capitalize(), "dollars")
print("По-русски:", num2words(tolov, lang='ru').capitalize(), "доллар(ов)")

