import random
def get_unique_list_numbers(start = -10, stop = 11, size = 15) -> list[int]:
    list_numbers = list(range(start, stop))  # TODO написать функцию для получения списка уникальных целых чисел
    random.shuffle(list_numbers)
    list_ = []
    for value in list_numbers:
            list_.append(value)
    return list_[:size]

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers))
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
