import os
import unittest
import time
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        super(TestLoginPage, self).setUp(self)
        # dzięki temu, będzie można użyć metody test_log_in_to_the_system np.
        # w test_add_a_player aby nie kopiować całości by się zalogować

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check if the title of the opened page is correct (login page)
        user_login.title_of_box()  # check if the title of the box is correct
        user_login.type_in_email('user07@getnada.com')  # enter "user07getnada@com" in the email field
        user_login.type_in_password('Test-1234')  # enter "Test-1234" in the password field
        user_login.click_on_the_sign_in_button()  # click on the sign in button

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()  # check if the title of the opened page is correct (dashboard)

        '''time.sleep (5)'''  # ta linia sprawia, że test zatrzymał się na 5 sekund,
        # a dopiero następnie zaczął wykonywać kolejne linie kodu. Ale tu zastępujemy ją Explicit wait

    @classmethod
    def tearDown(self):
        self.driver.quit()


    def test_changing_language_at_login_page(self):
        user_login = LoginPage(self.driver)
        user_login.click_on_the_language_select_menu_button()
        user_login.click_on_the_english_language_option()
        user_login.title_of_english_language_option()
        user_login.title_of_password_field_en()
        user_login.title_of_remind_password_field_en()
        user_login.title_of_sign_in_button_en()
        user_login.click_on_the_language_select_menu_button()
        user_login.click_on_the_polish_language_option()
        user_login.title_of_polish_language_option()
        user_login.title_of_password_field_pl()
        user_login.title_of_remind_password_field_pl()
        user_login.title_of_sign_in_button_pl()
        user_login.click_on_the_language_select_menu_button()
        user_login.click_on_the_english_language_option()
        user_login.title_of_english_language_option()
        user_login.title_of_password_field_en()
        user_login.title_of_remind_password_field_en()
        user_login.title_of_sign_in_button_en()


    def test_log_in_to_the_system_with_invalid_password(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.title_of_box()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('1234')
        user_login.click_on_the_sign_in_button()
        user_login.title_of_validation()



