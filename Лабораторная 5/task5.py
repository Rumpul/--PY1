import string
from random import sample

def get_random_password(password_leight = 8) -> str:
    all_letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return "".join(sample(all_letters, password_leight))
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
