from api.api import GoogleMapsAPI
from assertions.assert_methods import Assertions

"""Создание/Изменение/Удаление новой локации"""


def test_create_new_location():

    print("\n" + "=" * 50)
    print("\nМетод POST - Создание новой локации\n")
    # result_post: Response = GoogleMapsAPI.post_new_location()  # Старый способ
    result_post = GoogleMapsAPI.post_new_location()  # Новый способ

    check_post = result_post.json()
    place_id = check_post.get("place_id")

    Assertions.assert_status_code(result_post, 200)
    Assertions.assert_json_body_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
    print("\n" + "=" * 50 + "\n")

    print("Метод GET - Проверка метода POST\n")
    result_get = GoogleMapsAPI.get_new_location(place_id)

    Assertions.assert_status_code(result_get, 200)
    Assertions.assert_json_body_token(result_get, [
        'location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
    print("\n" + "=" * 50 + "\n")

    print("Метод PUT - Изменение новой локации\n")
    result_put = GoogleMapsAPI.put_new_location(place_id)

    Assertions.assert_status_code(result_put, 200)
    Assertions.assert_json_body_token(result_put, ['msg'])
    print("\n" + "=" * 50 + "\n")

    print("Метод GET - Проверка метода PUT\n")
    result_get = GoogleMapsAPI.get_new_location(place_id)

    Assertions.assert_status_code(result_get, 200)
    Assertions.assert_json_body_token(result_get, [
        'location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
    print("\n" + "=" * 50 + "\n")

    print("Метод DELETE - Удаление новой локации\n")
    result_delete = GoogleMapsAPI.delete_new_location(place_id)

    Assertions.assert_status_code(result_delete, 200)
    Assertions.assert_json_body_token(result_delete, ['status'])
    print("\n" + "=" * 50 + "\n")

    print("Метод GET - Проверка метода DELETE\n")
    result_get = GoogleMapsAPI.get_new_location(place_id)

    Assertions.assert_status_code(result_get, 404)
    Assertions.assert_json_body_token(result_get, ['msg'])
    print("\n" + "=" * 50 + "\n")

    print("Тестирование \"Создание/Изменение/Удаление новой локации\" завершено успешно")
