# from requests import Response


"""Методы для проверок ответов запрссов HTTP"""
import json


class Assertions:

    """Метод для проверки статус кода"""
    @staticmethod
    # def assert_status_code(response: Response, status_code):  # Старый способ
    def assert_status_code(result, status_code):  # Новый способ
        assert status_code == result.status_code
        print(f"\nСтатус-код = {result.status_code}, подтверждён")

    """Метод для проверки наличия обязательных полей в ответе запроса HTTP"""
    @staticmethod
    def assert_json_body_token(result, expected_value):
        json_body_token = json.loads(result.text)
        assert list(json_body_token) == expected_value
        print(f"\nОбязательный(-ые) ключ(-и) присутствует(-ют) в ответе запроса HTTP")

    """Метод для проверки значений обязательных полей в ответе запроса"""

    @staticmethod
    def assert_json_body_value(result, field_name, expected_value):
        json_body = result.json()
        json_body_value = json_body.get(field_name)
        assert json_body_value == expected_value
        print(f"{field_name} присутствует !!!")

    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""

    @staticmethod
    def assert_json_body_search_word_in_value(result, field_name, search_word):
        json_body = result.json()
        json_body_value = json_body.get(field_name)
        assert search_word in json_body_value
        print(f'Слово {search_word} присутствует!!!')
