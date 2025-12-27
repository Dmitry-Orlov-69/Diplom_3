import pytest
from selenium import webdriver
import requests
from helpers import random_email, random_name
from urls import DELETE_USER_ENDPOINT, LOGIN_ENDPOINT, REGISTER_ENDPOINT

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

@pytest.fixture
def unique_user():
    email = random_email()
    password = 'testpassword'
    name = random_name()

    # Регистрация пользователя
    response = requests.post(
        REGISTER_ENDPOINT,
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

        # Использование yield для автоматического удаления пользователя после теста
        yield user_data

        # Удаление пользователя после завершения теста
        requests.delete(
            DELETE_USER_ENDPOINT,
            json={
                "email": user_data['user_data']['email']
            }
        )
    else:
        pytest.fail(f"Failed to create user: {response.text}")
    
@pytest.fixture
def login_existing_user(unique_user):
    # Получение данных существующего пользователя
    email = unique_user['user_data']['email']
    password = unique_user['user_data']['password']

    # Попытка авторизоваться с существующим пользователем
    response = requests.post(
        LOGIN_ENDPOINT,
        json={
            "email": email,
            "password": password
        }
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['success'] is True
    assert 'accessToken' in response_data