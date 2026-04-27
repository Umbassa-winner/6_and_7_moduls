from playwright.sync_api import Page
import allure
from typing import Union
from playwright.sync_api import Locator
from tools.tools_create_dir_path import Tools

class PageAction:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Переход на страницу: {url}")
    def open_url(self, url: str):
        self.page.goto(url)


    @allure.step("Ввод текста '{text}' в поле '{locator}'")
    def enter_text_to_element(self, locator: Union[str, Locator], text: str):
        if isinstance(locator, str):
            self.page.fill(locator, text)
        else: locator.fill(text)


    @allure.step("Клик по элементу '{locator}'")
    def click_element(self, locator: Union[str, Locator]):
        if isinstance(locator, str):
            self.page.click(locator)
        else: locator.click()


    @allure.step("Ожидание загрузки страницы: {url}")
    def wait_redirect_for_url(self, url: str):
        self.page.wait_for_url(url)
        assert self.page.url == url, "Редирект на домашнюю старницу не произошел"


    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator: str) -> str:
        return self.page.locator(locator).text_content()


    @allure.step("Ожидание появления или исчезновения элемента: {locator}, state = {state}")
    def wait_for_element(self, locator: str, state: str = "visible"):
        self.page.locator(locator).wait_for(state=state)


    @allure.step("Скриншот текущей страницы")
    def make_screenshot_and_attach_to_allure(self):
        screenshot_path = Tools.files_dir('screenshots', 'screenshot.png')
        self.page.screenshot(path=screenshot_path, full_page=True)  # full_page=True для скриншота всей страницы

        # Прикрепление скриншота к Allure-отчёту
        with open(screenshot_path, "rb") as file:
            allure.attach(file.read(), name="Screenshot after redirect", attachment_type=allure.attachment_type.PNG)


    @allure.step("Проверка всплывающего сообщения c текстом: {text}")
    def check_pop_up_element_with_text(self, text: str) -> bool:

        notification_locator = self.page.get_by_text(text)
        # Ждем появления элемента
        notification_locator.wait_for(state="visible")
        assert notification_locator.is_visible(), "Уведомление не появилось"

        # Ждем, пока алерт исчезнет
        notification_locator.wait_for(state="hidden")
        assert notification_locator.is_visible() == False, "Уведомление не исчезло"