import random
import string


class Helpers:

    @staticmethod
    def generate_random_string(length=6):
        characters = string.ascii_lowercase
        random_string = ''
        for i in range(length):
            random_string += random.choice(characters)
        return random_string

    @staticmethod
    def generate_random_email(username="test"):
        digits = random.randint(100, 999)
        email = f"{username}_{digits}@yandex.ru"
        return email
