import random

def get_unique_list_numbers(start=-10, stop=11, size=15) -> list[int] :
      # TODO написать функцию для получения списка уникальных целых чисел
    if size <= len(range(start, stop)):
        list_numbers = []
        while len(list_numbers) < size:
            value = random.randint(start, stop)
            if value not in list_numbers:
                list_numbers.append(value)
        return list_numbers
    else:
        raise ValueError('Заданный размер списка больше, чем количество чисел в заданном диапазоне')

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers))
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
