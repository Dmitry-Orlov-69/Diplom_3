import pytest
from selenium import webdriver
import requests
import random
import string

@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    """Fixture for browser."""
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver
    driver.quit()

def random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + '@yandex.ru'

def random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

@pytest.fixture
def unique_user(request):
    email = random_email()
    password = 'testpassword'
    name = random_name()

    # Регистрация пользователя
    response = requests.post(
        'https://stellarburgers.education-services.ru/api/auth/register',
        json={
            "email": email,
            "password": password,
            "name": name
        }
    )

    if response.status_code == 200:
        user_data = {
            "user_data": {
                "email": email,
                "password": password,
                "name": name
            },
            "response": response.json()
        }

        # Определяем функцию для удаления пользователя после теста
        def delete_user():
            requests.delete(
                'https://stellarburgers.education-services.ru/api/auth/user',
                json={
                    "email": user_data['user_data']['email']
                }
            )

        # Добавляем финализатор для удаления пользователя
        request.addfinalizer(delete_user)

        return user_data
    else:
        raise Exception(f"Failed to create user: {response.text}")
    
@pytest.fixture
def login_existing_user(unique_user):
    # Получение данных существующего пользователя
    email = unique_user['user_data']['email']
    password = unique_user['user_data']['password']

    # Попытка авторизоваться с существующим пользователем
    response = requests.post(
        'https://stellarburgers.education-services.ru/api/auth/login',
        json={
            "email": email,
            "password": password
        }
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['success'] is True
    assert 'accessToken' in response_data