from playwright.sync_api import Page, expect
from models.base_page import BasePage


class CinescopeRegisterPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.url = f"{self.home_url}register"

        self.full_name_input = "input[name='fullName']"
        self.email_input = "input[name='email']"
        self.password_input = "input[name='password']"
        self.repeat_password_input = "input[name='passwordRepeat']"

        self.register_button = "//button[@type='submit' and text()='Зарегистрироваться']"
        self.sign_button = "//a[@href='/login' and text()='Войти']"

    # Локальные action методы
    def open(self):
        """Переход на страницу регистрации."""
        self.page.goto(self.url)

    # Вспомогательные action методы
    def register(self, full_name: str, email: str, password: str, confirm_password: str):
        """Полный процесс регистрации."""
        self.enter_text_to_element(self.full_name_input, full_name)
        self.enter_text_to_element(self.email_input, email)
        self.enter_text_to_element(self.password_input, password)
        self.enter_text_to_element(self.repeat_password_input, confirm_password)

        self.click_element(self.register_button)

    def assert_was_redirect_to_login_page(self):
        self.wait_redirect_for_url(f"{self.home_url}login")

    def assert_alert_was_pop_up(self):
        self.check_pop_up_element_with_text("Подтвердите свою почту")


class CinescopeLoginPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

        self.url = f'{self.home_url}login'

        # Локаторы формы
        self.email_field = 'input[type="email"]'
        self.password_field = 'input[name="password"]'
        self.login_button = '//button[@type="submit" and text()="Войти"]'
        self.register_button = page.get_by_role("link", name="Регистрация")

    # Локальные action методы
    def open(self):
        self.page.goto(self.url)

    # Вспомогательные action методы
    def login(self, email:str, password:str):
        self.enter_text_to_element(self.email_field, email)
        self.enter_text_to_element(self.password_field, password)

        self.click_element(self.login_button)

    def assert_redirect_to_home_page(self):
        self.wait_redirect_for_url(self.home_url)

    def assert_check_alert(self):
        self.check_pop_up_element_with_text("Вы вошли в аккаунт")