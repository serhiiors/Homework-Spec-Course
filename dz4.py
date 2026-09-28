# lvl 1.1, 1.2,
a = 17
b = 5
print(a + b, a - b, a * b, a / b )
print(a // b, a % b)
# // - це скільки разів число а поміщається в b
# % - це залишок від ділення a на b

# lvl 1.3
print(2 ** 10, 10 ** 3)

# lvl 1.4
price = 249
count = 3
print(price * count)

# lvl 1.5
print(type(7 / 2)) # повертає float, бо результат = 3.5(дробове число)
print(type(7 // 2)) # int бо результат ціле число
print(type(7.0 // 2)) #float бо дано дробове число 7.0

# lvl 1.6
name = "python"
result = " ".join(name.split() * 3)
print(result)

# lvl 1.7
hello = "Привіт "
world = "світ!"
result = hello + world
print(result)

#lvl 2.8
students = 28
desk = 6
print("Буде повних рядів: ", students // desk, "\nЗалишилось учнів: ", students % desk)

#lvl 2.9
seconds = 3725
hours = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
secs = rest % 60
print(hours, "год", minutes, "хв", secs, "с")

#lvl 2.10
minutes = 150
hours = minutes // 60
mins = minutes % 60
print (hours, "hours", mins, "minutes")

#lvl 2.11
c = 36.6
f = c * 9 / 5 + 32
print(f)

#lvl 2.12
a = 12.5
b = 8
area = a * b
perimeter = (a * 2) + (b * 2)
print("Area: ", area, "Perimeter: ", perimeter)

#lvl 2.13
r = 7
pi = 3.14159
area1 = pi * r ** 2
print(area1)

#lvl 2.14
price = 1200
discount = price * 15/ 100
print("Сума зі знижкою: ", price - discount)

#lvl 2.15
salary = 25000
tax = salary * 19.5 / 100
print("profit: ", salary - tax)

#lvl 2.16
speed = 90
t = 2.5
print("Distance: ", speed * t )

#lvl 2.17
print((10 + 11 + 8) / 3)

#lvl 3.18
n = 7
if(n % 2 == 0):
    print("парне")
else:
    print("непарне")

#lvl 3.19
n = 473
print(n % 10)

#lvl 3.20
n = 473

hundreds = n // 100
tens = n // 10 % 10
units = n % 10

print("Сотні:", hundreds, "Десятки:", tens, "Одиниці:", units)

#lvl 3.21
n = 859
hundreds = n // 100
tens = n // 10 % 10
units = n % 10
total = hundreds + tens + units
print(total)

#lvl 3.22
n = 123
hundreds = n // 100
tens = n // 10 % 10
units = n % 10
reversed_n = units * 100 + tens * 10 + hundreds
print(reversed_n)

#lvl 3.23
print(144 ** 0.5)

#lvl 3.24
print(365 * 24 * 60 * 60)

#lvl 3.25
x = "5"
y = "3"
print(x + y) ## Тут тип даних String тобто це зчитуєтсь як слова, а їх додати неможливо
x = 3
y = 5
print(x + y) ## Тут вже integer, тобто зчитується як числа

#lvl 3.26
num = (int(9.99))
print(num) ## дробова частина зникла, адже інт підтримує лише цілі числа

#lvl 3.27
print(True + True + True) ## бо True == 1, false == 0
print(True * 10)

#lvl 3.28
a = 5
b = 10
a = a + b
b = a - b
a = a - b
print(a, b)

#lvl 3.29
deposit = 10000
rate = 0.12
sum = deposit * (1 + 0.12) ** 3
print(sum)

#lvl 3.30
symbol = "-"
num = 20
print(symbol * num)
print("Result: " " 2 ** 20")