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

