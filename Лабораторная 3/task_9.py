salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
total_money = spend
for i in range (2, months + 1):
    spend *= 1.03
    total_money +=spend
need_money = total_money - salary * 10
print(round(need_money))
