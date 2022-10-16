from random import sample

def get_random_password() -> str:
    password_leight = 8
    numbers = '0123456789'
    upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_char = 'abcdefghijklmnopqrstuvwxyz'
    simbols = '!#$%&*+-=?@^_'
    all_letters = numbers + upper_char + lower_char + simbols
    return "".join(sample(all_letters, password_leight))
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
