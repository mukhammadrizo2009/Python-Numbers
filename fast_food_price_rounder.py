from num2words import num2words
from decimal import Decimal

food1 = Decimal(input("Birinchi mahsulot narxini kiriting($): "))
food2 = Decimal(input("Ikkinchi mahsulot narxini kiriting($): "))
food3 = Decimal(input("Uchunchi mahsulot narxini kiriting($): "))

total = food1+food2+food3

print(f"Umumiy narx: ${total:.2f} ({num2words(total, lang='en', to='currency', currency='USD')}. {num2words(total, lang='ru', to='currency', currency='USD')})")
print(f"Yaxlitlangan narx: ${round(total, 1)} ({num2words(total, lang='en', to='currency', currency='USD')}. {num2words(total, lang='ru', to='currency', currency='USD')})")


