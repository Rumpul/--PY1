money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
total_money = money_capital + salary

while total_money >= 0:
    total_money -= spend + spend * 0.05
    month += 1
print(month)
