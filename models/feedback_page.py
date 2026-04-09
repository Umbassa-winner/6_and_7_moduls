from models.base_page import BasePage
from playwright.sync_api import Page
import allure

class FeedbackPage(BasePage):

    def __init__(self, page:Page, film_id:str, film_score:str):
        super().__init__(page)

        self.url = f"{self.home_url}movies/{film_id}"

        self.area_for_feedback = page.get_by_role("textbox", name="Написать отзыв")
        self.combox_button = page.get_by_role("combobox")

        allow_score = ["1", "2", "3", "4", "5"]
        assert film_score in allow_score, f'Выбранная оценка фильма: {film_score}, вне range {allow_score}'

        self.combox_point = page.get_by_role("option", name=film_score)

        self.send_button = page.get_by_role("button", name="Отправить")

    @allure.step("Проверка, что текст отзыва опубликовался")
    def assert_complete_published_feedback(self, text: str):
        self.page.get_by_text(text)

    @allure.step("Проверка, что оценка отзыва опубликовалась")
    def assert_complete_published_feedback_rate(self, point: str):
        self.page.get_by_text(point)