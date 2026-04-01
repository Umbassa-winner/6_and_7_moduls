import time
from playwright.sync_api import Page, expect
from datetime import datetime

class TestSelector:

    def test_codegen_code(self, page: Page):

        page.goto("https://demoqa.com")

        page.locator("svg").first.click()
        page.get_by_text("Text Box").click()

        page.get_by_role("textbox", name="Full Name").fill("Name_example")
        page.get_by_role("textbox", name="name@example.com").fill("main@example.ru")
        page.get_by_role("textbox", name="Current Address").fill("Address")
        page.locator("#permanentAddress").fill("address")

        page.get_by_role("button", name="Submit").click()

        expect(page.locator("#name")).to_contain_text("Name:Name_example")
        expect(page.locator("#email")).to_contain_text("Email:main@example.ru")
        expect(page.locator("#output")).to_contain_text("Current Address :Address")
        expect(page.locator("#output")).to_contain_text("Permananet Address :address")

        time.sleep(5)

class TestLocators:

    def test_class_selector(self, page):
        page.goto('https://the-internet.herokuapp.com/login')

        i = page.locator('.subheader')

        expect(i).to_be_visible()
        expect(i).to_contain_text('This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages.')
        expect(i).to_have_count(1)

    def test_id_selector(self, page):
        page.goto('https://the-internet.herokuapp.com/login')

        i = page.locator('#username')
        i.fill('Луи Армстронг')

        expect(i).to_be_visible()
        expect(i).to_have_value('Луи Армстронг')
        expect(i).to_have_count(1)

    def test_has_text_selector(self, page):
        page.goto('https://the-internet.herokuapp.com/login')

        i = page.locator('label:has-text("Password")')

        expect(i).to_be_visible()
        expect(i).to_have_count(1)

    def test_teg_text_selector(self, page):
        page.goto('https://the-internet.herokuapp.com/login')

        i = page.locator('i', has_text=' Login')

        expect(i).to_be_visible()
        expect(i).to_have_count(1)

    def test_only_text_selector(self, page):
        page.goto('https://the-internet.herokuapp.com/login')

        i = page.locator("*", has_text=' Login')

    def test_only_teg_selector(self, page):
        page.goto('https://dev-cinescope.coconutqa.ru/register')

        i = page.locator('input').all()
        print(f"Найдено элементов: {len(i)}")


        for j, k in enumerate(i):
            print(f"Элемент № {j}: {k}")

    def test_teg_and_attribute_selector(self, page):

        page.goto("https://dev-cinescope.coconutqa.ru/register")

        i = page.locator('input[name="fullName"]')

        expect(i).to_be_visible()
        expect(i).to_have_count(1)
        expect(i).to_be_editable()


class TestLocatorsGetBy:

    def test_button_add(self, page):
        # 1. К кнопке add нужно обратиться используя несколько методов:
        #     1. Это должен быть <button>
        #     2. иметь текст “Add”
        #     3. После нахождения локатора используем метод .click()

        page.goto('https://demoqa.com/webtables')

        add_button = page.get_by_role("button", name="Add")
        add_button.click()

        # 1. Убедиться что она открылась - используя метод is_visible
        # 2. Для определения локатора, нужно произвести поиск по вложенным элементам.
        # Например, чтобы в заголовке модального окна, был текст “Registration Form”

        registration_form_headaer = page.get_by_text("Registration Form")
        assert registration_form_headaer.is_visible()

        # 3. Заполнить первый инпут следующим образом:
        #     1. Использовать метод .fill()
        #     2. Определить локатор как: инпут, имеющий плейсхолдер “First Name”

        first_input = page.get_by_placeholder("First Name")
        first_input.fill("Billy Herrington")


        # 4. Заполнить все остальные поля, обращаясь к локаторам, как вам удобно.
        form = page.locator("#userForm input").all()

        for field in form:

            placeholder = field.get_attribute("placeholder")

            if placeholder == "First Name":
                continue
            elif placeholder == "name@example.com":
                field.fill("test@gmail.com")
            elif placeholder == "Age":
                field.fill("99")
            elif placeholder == "Salary":
                field.fill("999999")
            else: field.fill("Тестовое значение")

        # 5. Нажать кнопку submit

        page.get_by_role("button", name="Submit").click()

        time.sleep(3)


class TestActions:

    def test_form_with_actions(self, page):
        # 1. Заполнить полностью форму.
        #     1. Для заполнения пробуйте использовать page.fill() и page.type() и посмотрите разницу.
        #     2. На странице есть чек боксы, есть радиобатоны и выпадающие списки - со всем этим необходимо повзаимодействовать.
        # 2. Для поля “Date of birth” что на скриншоте,
        #     1. нужно убедиться, что значение по умолчанию == сегодня.
        #     2. Значение из value нужно достать при помощи page.get_attribute()
        # 3. Из футера нужно достать текст и сделать ассерт, что он совпадает

        page.goto("https://demoqa.com/automation-practice-form")

        page.get_by_placeholder("First Name").fill("Билли")
        page.type("#lastName", "Херрингтон")
        page.get_by_placeholder("name@example.com").fill("test@gmail.com")
        page.check("#gender-radio-1")
        page.get_by_placeholder("Mobile Number").fill("8999999999")
        assert page.locator("#dateOfBirthInput").get_attribute("value") == datetime.now().strftime("%d %b %Y")
        page.check("#hobbies-checkbox-1")
        page.check("#hobbies-checkbox-3")
        state_input = page.locator("#react-select-3-input")
        state_input.fill("NCR")
        state_input.press("Enter")



        time.sleep(3)


class TestWaitorsAndConditions:

    def test_radio_button(self, page):

        # Задание №1: https://demoqa.com/radio-button, написать тест на проверку активности элементов:
            # 1. проверка активности 2 радиобаттонов и неактивности 3-го - https://disk.yandex.ru/i/f0NwfPnNQeFeiw

        page.goto("https://demoqa.com/radio-button")

        assert page.is_enabled("#yesRadio") == True
        assert page.is_enabled("#impressiveRadio") == True
        assert page.is_enabled("#noRadio") == False

    def test_cheeckbox(self, page):

        # Задание №2: # https://demoqa.com/checkbox. Написать тест на проверку видимости элементов:

            # 1. Написать проверку, что Home виден, а Desktop не виден - https://disk.yandex.ru/i/DaTEP9xbyd3Caw
            # 2. Произвести клик по тогглу раскрыв список
            # 3. Сделать проверку, что Desktop видел - https://disk.yandex.ru/i/fohm9ofQ4xXgvg

        page.goto("https://demoqa.com/checkbox")
        assert page.is_hidden('[aria-label="Select Desktop"]') == True

        page.locator('.rc-tree-switcher').click()
        assert page.is_hidden('[aria-label="Select Desktop"]') == False

        time.sleep(3)

    def test_dynamic_properties(self, page):
        pass

        # Задание №3 https://demoqa.com/dynamic-properties
            # Через 5 секунд после загрузки страницы появится элемент - https://disk.yandex.ru/i/YzzeSOPGMqfpNw
            # Написать тест, который:
                # 1. Убедится что элемента нет на странице
                # 2. Дождаться элемент используя page.wait_for_selector()

        page.goto("https://demoqa.com/dynamic-properties")

        assert page.is_hidden('#visibleAfter') == True

        i = page.wait_for_selector('#visibleAfter', state='visible')

    def test_expect(self, page):

        page.goto("https://demoqa.com/radio-button")

        yes_radio = page.get_by_role("radio", name="Yes")
        impressive_radio = page.get_by_role("radio", name="Impressive")
        no_radio = page.get_by_role("radio", name="No")

        expect(no_radio).to_be_disabled()  # проверяем, что не доступен
        expect(yes_radio).to_be_enabled()  # проверяем, что доступен
        expect(impressive_radio).to_be_enabled()  # проверяем, что доступен

        page.locator('[for="yesRadio"]').click()  # тут хитрый лейбл не позволяет кликнуть прямо на инпут, обращаемся по лейблу
        expect(yes_radio).to_be_checked()  # проверяем, что отмечен
        expect(impressive_radio).not_to_be_checked()  # проверяем, что не отмечен