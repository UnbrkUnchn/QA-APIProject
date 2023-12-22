import requests


"""Список HTTP Методов"""


class HttpMethods:

    headers = {'Content-Type': 'application/json'}
    cookies = ""

    """Кастомный метод GET"""
    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    """Кастомный метод POST"""
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    """Кастомный метод PUT"""
    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    """Кастомный метод DELETE"""
    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result
