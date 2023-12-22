from utilities.http_methods import HttpMethods

"""Методы для тестирования Google Maps API"""

base_url = "https://rahulshettyacademy.com"  # Базовая  URL для всех методов
key = "?key=qaclick123"  # Параметр для всех методов


class GoogleMapsAPI:

    """Метод для создания новой локации"""
    @staticmethod
    def post_new_location():

        resource_post = "/maps/api/place/add/json"  # Ресурс (URN) метода POST
        url_post = f"{base_url}{resource_post}{key}"
        print(f"Текущий URL метода POST:\n{url_post}\n")

        json_body_post = \
            {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                            },
                "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                         ],
                "website": "http://google.com",
                "language": "French-IN"
            }

        result_post = HttpMethods.post(url_post, json_body_post)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_location(place_id):

        resource_get = "/maps/api/place/get/json"  # Ресурс (URN) метода GET
        url_get = f"{base_url}{resource_get}{key}&place_id={place_id}"
        print(f"Текущий URL метода GET:\n{url_get}\n")

        result_get = HttpMethods.get(url_get)
        print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_location(place_id):

        resource_put = "/maps/api/place/update/json"  # Ресурс (URN) метода PUT
        url_put = f"{base_url}{resource_put}{key}&place_id={place_id}"
        print(f"Текущий URL метода PUT:\n{url_put}\n")

        json_body_put = \
            {
                "place_id": place_id,
                "address": "100 Lenina street, RU",
                "key": "qaclick123"
            }

        result_put = HttpMethods.put(url_put, json_body_put)
        print(result_put.text)
        return result_put

    """Метод для удаления новой локации"""
    @staticmethod
    def delete_new_location(place_id):

        resource_delete = "/maps/api/place/delete/json"
        url_delete = f"{base_url}{resource_delete}{key}&place_id={place_id}"
        print(f"Текущий URL метода DELETE:\n{url_delete}\n")

        json_body_delete = \
            {
                "place_id": place_id
            }

        result_delete = HttpMethods.put(url_delete, json_body_delete)
        print(result_delete.text)
        return result_delete
