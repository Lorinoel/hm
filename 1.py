import random
import math
m=0
name= input("Введіть ім'я -")
age= int(input("Введіть вік -"))
print(f"Привіт {name}, тобі {age}!")
if age>=18:
    print("Вхід дозволенло!")
else:
    print("Вхід заборонено!")
print ("Гра - Вгадай число")
n = random.randint(1, 10)
u =0
while m<=3:
    m = m + 1
    u = int(input("Введіть число від 1 до 10 -"))
    if n == u:
        print(f"Число, що загадав комп'ютер - {n}")
        print(f"Ваше число - {u}")
        print("Ви виграли")
        break
    elif m==3:
        print('Заблоковано')
        print(f"Число, що загадав комп'ютер - {n}")
        print(f"Ваше число - {u}")
        break
    elif u<1 or u>10:
        print("Число не підходить")
    elif not n==u:
        if n>u:
            print("Більше")
        if n< u:
            print("Менше")
print("Програма, яка пише числа")
a = int(input("Введіть число з якого почнається рахунок -"))
b = int(input("Введіть число яким закінчиться рахунок -"))
for i in range(b-a):
    while a!=b:
        a=a+1
        print(a, end=" ")
print("\nПрограму, яка виводить на екран тільки парні числа")
c = int(input("Введіть число -"))

for i in range(c, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")
print("\nПрограма, яка рахує факторіал")
d = int(input("Введіть число - "))
print("Факторіал - ", math.factorial(d))
print("Програма, яка визначить оцінку")
e = int(input("Введіть оцінку - "))
if e>=0 and e<=49:
    print("Незадовільно")
elif e>=50 and e<=69:
    print("Задовільно")
elif e>=70 and e<=89:
    print("Добре")
elif e>=90 and e<=100:
    print("Відмінно")
else:
    print("Такої оцінки немає")
print("Калькулятор")
f = float(input("Введіть перше число (a)- "))
g = float(input("Введіть друге число (b)- "))

o = input("Введіть математичну дію (+, -, *, /)- ")

if o == "+":
    result = f + g
    print("Результат-", result)

elif o == "-":
    result = f - g
    print("Результат-", result)

elif o == "*":
    result = f * g
    print("Результат-", result)

elif o == "/":
    if g == 0:
        print("Ділення на нуль")
    else:
        result = f / g
        print("Результат-", result)

else:
    print("Невірна математична дія")
