MAIN_PAGE_URL = "https://stellarburgers.education-services.ru"  # главная страница
LOGIN_URL = f"{MAIN_PAGE_URL}/login"  # страница входа/авторизации
ORDER_FEED_PAGE_URL = f"{MAIN_PAGE_URL}/feed"  # страница ленты заказов

REGISTER_ENDPOINT = f"{MAIN_PAGE_URL}/api/auth/register"
DELETE_USER_ENDPOINT = f"{MAIN_PAGE_URL}/api/auth/user"
LOGIN_ENDPOINT = f"{MAIN_PAGE_URL}/api/auth/login"