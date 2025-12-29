import random
import string

def random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + '@yandex.ru'

def random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))