import random
import string
from faker import Faker
from datetime import datetime
from uuid import uuid4
import requests

faker = Faker()
class DataGenerator:

# """ ============================== API AUTH ================================== """

    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"kek{random_string}@gmail.com"


    @staticmethod
    def generate_random_name():
        return f"{faker.first_name()} {faker.last_name()}"


    @staticmethod
    def generate_random_password():
        """
        Генерация пароля, соответствующего требованиям:
        - Минимум 1 буква.
        - Минимум 1 цифра.
        - Допустимые символы.
        - Длина от 8 до 20 символов.
        """
        # Гарантируем наличие хотя бы одной буквы и одной цифры
        letters = random.choice(string.ascii_letters)  # Одна буква
        digits = random.choice(string.digits)  # Одна цифра

        # Дополняем пароль случайными символами из допустимого набора
        special_chars = "?@#$%^&*|:"
        all_chars = string.ascii_letters + string.digits + special_chars
        remaining_length = random.randint(6, 18)  # Остальная длина пароля
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))

        # Перемешиваем пароль для рандомизации
        password = list(letters + digits + remaining_chars)
        random.shuffle(password)

        return ''.join(password)

# """ ============================== API MOVIES ================================== """

    @staticmethod
    def generate_random_movie_name():
        return f"{faker.word()} {faker.word()}".capitalize()

    @staticmethod
    def generate_image_url():
        return faker.url()

    @staticmethod
    def generate_movie_price():
        return random.randint(10000, 20000)

    @staticmethod
    def generate_movie_description():
        return f"This movie about {faker.sentence().lower()}"

    @staticmethod
    def generate_movie_location():

        return random.choice(["SPB", "MSK"])

    @staticmethod
    def generate_movie_published():
        return random.choice([True, False])

    @staticmethod
    def generate_movie_ganreid():

        """
        Кто-то удалил жанры 5 и 6, поэтому решил автоматизировать этот процесс, теперь используются только те жанры, которые по факту есть в БД
        """

        resp = requests.request(method="GET",
                                url="https://api.dev-cinescope.coconutqa.ru/genres").json()
        i = [genre.get('id') for genre in resp]
        sorted_list = sorted(i)

        return random.choice(sorted_list)

    @staticmethod
    def generate_movie_max_price():
        return random.randint(5000, 10000)

    @staticmethod
    def generate_movie_min_price():
        return random.randint(1000, 4999)

    @staticmethod
    def generate_admin_creds():
        return ("api1@gmail.com", "asdqwe123Q")

# """ ============================== NEGATIEVE API MOVIES ================================== """


    @staticmethod
    def generate_negative_movie_max_price():
        return faker.name()

    @staticmethod
    def generate_negative_movie_min_price():
        return faker.name()

    @staticmethod
    def generate_negative_random_word():
        return faker.word()

    @staticmethod
    def generate_negative_random_id():
        return faker.random_int(800000000, 900000000)

# """ ============================== DATABASE  ================================== """

    @staticmethod
    def generate_movie_data_for_orm_model() -> dict:
        """Генерирует данные для тестового фильма"""

        return {
            "name": DataGenerator.generate_random_name(),
            "price": DataGenerator.generate_movie_price(),
            "description": DataGenerator.generate_movie_description(),
            "image_url": DataGenerator.generate_image_url(),
            "location": DataGenerator.generate_movie_location(),
            "published": DataGenerator.generate_movie_published(),
            "rating": DataGenerator.generate_movie_min_price(),
            "genre_id": DataGenerator.generate_movie_ganreid(),
            "created_at": datetime.now()
        }

    @staticmethod
    def generate_random_int():
        return faker.random_int()