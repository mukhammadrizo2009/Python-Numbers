from num2words import num2words

masofa = float(input("Masofani kiriting: "))

oldindan_tolov = 5.00
km_uchun = 0.80

result = masofa + oldindan_tolov * km_uchun
result = round(result , 2)

print("Ohirgi to'lov: $",result)

print("In russian:", num2words(result, to='currency', lang='ru'))
print("In english:", num2words(result, to='currency', lang='en'))