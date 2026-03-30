import time
from playwright.sync_api import Page, expect

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

    def test_button(self):
        pass