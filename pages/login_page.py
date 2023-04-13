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

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

