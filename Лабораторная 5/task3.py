import random
def get_unique_list_numbers() -> list[int]:
    list_numbers = list(range(-10, 11))  # TODO написать функцию для получения списка уникальных целых чисел
    random.shuffle(list_numbers)
    max_count_nember = 15
    list_ = []
    for value in list_numbers:
            list_.append(value)
    return list_[:max_count_nember]

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers))
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
