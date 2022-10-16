
def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()

    for sim in str_:
        if sim.isalpha() == True:
            dict_[sim] = dict_.get(sim, 0) + 1

    return dict_
# TODO посчитать количество каждой буквы в строке в аргументе str_
def percent_count_char(dict_):
    new_dict = {}
    total_count = sum(dict_.values())
    for sim, count in dict_.items():
        new_dict[sim] = (count/total_count)*100
    return new_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_ = get_count_char(main_str)
print(get_count_char(main_str))
print(percent_count_char(dict_))
