src = not False and True or False and not True

# TODO расписать упрощение выражения
#избавляемся от отицаний:  result = True and True or False and False
#избавляемся от логического "И" : result =True or False
#збавляемся от логического "ИЛИ": result = True
result = True  # TODO подставить результат выражения

print(src == result)
