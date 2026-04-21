import pytest
from tools.tools_create_dir_path import Tools
from models.register_page_and_login_page import CinescopeLoginPage
from resources.user_creds import CommonUserCreds
import os
from utils.data_generator import DataGenerator


DEFAULT_UI_TIMEOUT = 30000

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def base_context(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.set_default_timeout(DEFAULT_UI_TIMEOUT)
    yield context
    log_name = f"trace_{Tools.get_timestamp()}.zip"
    trace_path = Tools.files_dir('playwright_trace', log_name)
    context.tracing.stop(path=trace_path)
    context.close()

@pytest.fixture(scope="function")
def base_page(base_context):
    page = base_context.new_page()
    yield page
    page.close()

"""=========================================== FEEDBACK page  =============================================="""


@pytest.fixture(scope="session")
def get_auth_context(playwright):
    """ Получение кук после авторизации для автом. авторизации и запись в файл """

    auth_path = os.path.join(os.getcwd(), "auth.json")

    silent_browser = playwright.chromium.launch(headless=True)
    context = silent_browser.new_context()
    page = context.new_page()

    login_page = CinescopeLoginPage(page)
    login_page.open()
    login_page.login(CommonUserCreds.EMAIL, CommonUserCreds.PASSWORD)  # Осуществляем вход
    page.wait_for_load_state("networkidle")
    context.storage_state(path="auth.json")

    context.close()
    silent_browser.close()

    yield True

    if os.path.exists(auth_path):
        os.remove(auth_path)

@pytest.fixture(scope="function")
def context_with_auth(get_auth_context, browser):
    """ Создание контекста с авторизацией """

    auth_path = os.path.join(os.getcwd(), "auth.json")

    context = browser.new_context(storage_state=auth_path)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.set_default_timeout(DEFAULT_UI_TIMEOUT)
    yield context
    log_name = f"trace_{Tools.get_timestamp()}.zip"
    trace_path = Tools.files_dir('playwright_trace', log_name)
    context.tracing.stop(path=trace_path)
    context.close()


@pytest.fixture(scope="function")
def page_with_auth(context_with_auth):
    """ Создание страницы с авторизацией """
    page = context_with_auth.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def create_text_to_feedback():
    """ Создание текста для вписания в поле отзыва """

    return DataGenerator.generate_movie_description()

@pytest.fixture(scope="function")
def film_score():
    """ Создание рандомной оценки фильма от 1 до 5 """

    return f"{DataGenerator.generate_random_film_score()}"
