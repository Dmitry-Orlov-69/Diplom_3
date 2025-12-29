from selenium.webdriver.common.by import By

BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # кнопка "Конструктор"
INGREDIENT_BUN_R2_D3 = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__text__yp3dH:contains('Флюоресцентная булка R2-D3')") # ингредиент "Флюоресцентная булка R2-D3"
MODAL_INGREDIENT_DETAILS = (By.CSS_SELECTOR, ".Modal_modal__contentBox__sCy8X.pt-10.pb-15") # Окно с деталями ингредиента
TEXT_INGREDIENT_DETAILS = (By.CSS_SELECTOR, ".Modal_modal__title_modified__3Hjkd.Modal_modal__title__2L34m:contains('Детали ингредиента')") # надпись "детали ингредиента"
CLOSED_INGREDIENT_DETAILS_MODAL_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__title_modified__3Hjkd ~ .Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK") # Крестик, закрывающий окно с деталями ингредиента
COUNTER_BUN_R2_D3 = (By.XPATH, "//p[@class='counter_counter__num__3nue1']") # Счётчик ингредиента «Флюоресцентная булка R2-D3»
ORDER_COLLECTION_FIELD = (By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7.mt-25") # Поле сбора заказа
BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # Кнопка «Оформить заказ»
ORDER_MODAL = (By.CSS_SELECTOR, ".Modal_modal__contentBox__sCy8X.pt-30.pb-30") # окно заказа
ORDER_ID_IN_MODAL = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m']") # Идентификатор заказа в окне заказа
CLOSED_ORDER_MODAL_BUTTON = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 .Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK") # крестик, закрывающий окно заказа
BUTTON_ORDER_FEED = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]") # Кнопка «Лента заказов»
COUNTER_ALL_TIME = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ.text.text_type_digits-large") # Счётчик «Выполнено за всё время»
COUNTER_TODAY = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ.text.text_type_digits-large[class='OrderFeed_number__2MbrQ']") # Счётчик «Выполнено за сегодня»
ORDER_IN_PROGRESS = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']") # Номер заказа в работе