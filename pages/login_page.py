import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']//child::span[1]"
    remind_password_hyperlink_xpath = "//a[@tabindex='-1']"
    scouts_panel_header_xpath = "//div/h5"
    language_select_menu_xpath = "//div[@tabindex='0']"
    polish_language_option_xpath = "//ul/li[1]"
    english_language_option_xpath = "//ul/li[2]"
    login_url = "https://scouts-test.futbolkolektyw.pl/en/"
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//form/div/div[1]/h5"
    expected_title_of_box = "Scouts Panel"
    expected_title_of_polish_language_option = "Polski"
    expected_title_of_english_language_option = "English"
    title_of_polish_language_option_xpath = "//div[2]/div/div"
    title_of_english_language_option_xpath = "//div[2]/div/div"
    expected_title_of_password_field_in_polish = "Hasło"
    expected_title_of_password_field_in_english = "Password"
    title_of_password_field_xpath = "//*[@id = 'password-label']"
    expected_title_of_remind_password_button_in_polish = "Przypomnij hasło"
    expected_title_of_remind_password_button_in_english = "Remind password"
    title_of_remind_password_button_xpath = "//div/div[1]/a"
    expected_title_of_sign_in_button_in_polish = "ZALOGUJ"
    expected_title_of_sign_in_button_in_english = "SIGN IN"
    title_of_sign_in_button_xpath = "//button/span[1]"
    expected_title_of_validation = "Identifier or password invalid."
    title_of_validation_xpath = "//div[3]/span"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def title_of_box(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.expected_title_of_box)

    def click_on_the_language_select_menu_button(self):
        self.click_on_the_element(self.language_select_menu_xpath)

    def click_on_the_polish_language_option(self):
        self.click_on_the_element(self.polish_language_option_xpath)

    def click_on_the_english_language_option(self):
        self.click_on_the_element(self.english_language_option_xpath)

    def title_of_polish_language_option(self):
        self.assert_element_text(self.driver, self.title_of_polish_language_option_xpath,
                                 self.expected_title_of_polish_language_option)

    def title_of_english_language_option(self):
        self.assert_element_text(self.driver, self.title_of_english_language_option_xpath,
                                 self.expected_title_of_english_language_option)

    def title_of_password_field_pl(self):
        self.assert_element_text(self.driver, self.title_of_password_field_xpath,
                                 self.expected_title_of_password_field_in_polish)

    def title_of_password_field_en(self):
        self.assert_element_text(self.driver, self.title_of_password_field_xpath,
                                 self.expected_title_of_password_field_in_english)

    def title_of_remind_password_field_pl(self):
        self.assert_element_text(self.driver, self.title_of_remind_password_button_xpath,
                                 self.expected_title_of_remind_password_button_in_polish)

    def title_of_remind_password_field_en(self):
        self.assert_element_text(self.driver, self.title_of_remind_password_button_xpath,
                                 self.expected_title_of_remind_password_button_in_english)

    def title_of_sign_in_button_pl(self):
        self.assert_element_text(self.driver, self.title_of_sign_in_button_xpath,
                                 self.expected_title_of_sign_in_button_in_polish)

    def title_of_sign_in_button_en(self):
        self.assert_element_text(self.driver, self.title_of_sign_in_button_xpath,
                                 self.expected_title_of_sign_in_button_in_english)

    def title_of_validation(self):
        self.assert_element_text(self.driver, self.title_of_validation_xpath,
                                 self.expected_title_of_validation)

    def select_language(self, language):
        self.click_on_the_element(self.language_select_menu_xpath)
        time.sleep(1)
        if language == "English":
            self.click_on_the_element(self.title_of_english_language_option_xpath)
        else:
            self.click_on_the_element(self.title_of_polish_language_option_xpath)
