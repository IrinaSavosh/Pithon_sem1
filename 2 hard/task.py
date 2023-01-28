#Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.

number = float(input("Введите любое вещественное или целое число: "))

while number % 10 != 0:
   number *= 10

number = int(number)
sum = 0
while number > 0:
   sum = sum + number % 10
   number //= 10

print(sum)
