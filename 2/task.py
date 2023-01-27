# Найдите сумму цифр трехзначного числа.
sum = 0
number = int(input("Введите трехзначное число: "))
if number > 99 and number < 1000:
   while number != 0:
      sum = sum + number % 10
      number //= 10
      #print(number)
   print(sum)
else:
   print("Вы ввeли не трехзначное число")

