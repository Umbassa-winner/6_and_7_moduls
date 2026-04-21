from models.feedback_page import FeedbackPage
import time
from playwright.sync_api import Page
import allure
import pytest

@allure.epic("Тестирование UI")
@allure.feature("Тестирование страницы с отзывами")
@pytest.mark.ui
class TestFeedbackPage:

    @allure.title("Проведение успешной попытки оставить отзыв с оценкой")
    def test_feedback_page(self, page_with_auth:Page, create_text_to_feedback, film_score):

        feedback_page = FeedbackPage(page_with_auth, film_id="39587", film_score=film_score)

        feedback_page.open()

        feedback_page.enter_text_to_element(feedback_page.area_for_feedback, create_text_to_feedback)

        feedback_page.click_element(feedback_page.combox_button)

        feedback_page.click_element(feedback_page.combox_point)

        feedback_page.click_element(feedback_page.send_button)

        feedback_page.check_pop_up_element_with_text('Отзыв успешно создан')

        feedback_page.assert_complete_published_feedback(create_text_to_feedback)

        feedback_page.assert_complete_published_feedback_rate(film_score, create_text_to_feedback)

        # УБРАТЬ ПОСЛЕ ДЕБАГА
        time.sleep(1)




