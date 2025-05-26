from num2words import num2words


masofa = float(input("Masofani kiriting (km): "))


boshlangich_tolov = 3.00
km_ga = 1.20

total = boshlangich_tolov + masofa * km_ga
total = round(total, 2)  


print("Yakuniy to‘lov: $", total)


print("In english:", num2words(total, to='currency', lang='en'))


print("In russian:", num2words(total, to='currency', lang='ru'))

