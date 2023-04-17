from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    add_player_form_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    email_field_xpath = "//div[1]/div/div/input"
    name_field_xpath = "//div[2]/div/div/input"
    surname_field_xpath = "//div[3]/div/div/input"
    phone_field_xpath = "//div[4]/div/div/input"
    weight_field_xpath = "//div[5]/div/div/input"
    height_field_xpath = "//div[6]/div/div/input"
    date_of_birth_field_xpath = "//div[7]/div/div/input"
    leg_select_menu_xpath = '//*[@id="mui-component-select-leg"]'
    right_leg_option_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    left_leg_option_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    club_field_xpath = "//div[9]/div/div/input"
    level_field_xpath = "//div[10]/div/div/input"
    main_position_field_xpath = "//div[11]/div/div/input"
    second_position_field_xpath = "//div[12]/div/div/input"
    district_select_menu_field_xpath = "//*[@id='mui-component-select-district']"
    lodz_district_option_xpath = "//*[@data-value='lodzkie']"
    achievements_field_xpath = "//div[14]/div/div/input"
    add_language_button_xpath = "//div[15]/button/span[1]"
    language_field_xpath = "//div[15]/div/div/div/input"
    add_youtube_link_button_xpath = "//div[19]/button/span[1]"
    youtube_field_xpath = "//*[@name='webYT[0]']"
    submit_button_xpath = "//div[3]/button[1]/span[1]"

    def title_of_page(self):
        assert self.get_page_title(self.add_player_form_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone_number):
        self.field_send_keys(self.phone_field_xpath, phone_number)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_date_of_birth(self, date_of_birth):
        self.field_send_keys(self.date_of_birth_field_xpath, date_of_birth)

    def click_on_the_leg_select_menu(self):
        self.click_on_the_element(self.leg_select_menu_xpath)

    def click_on_the_right_leg_option(self):
        self.click_on_the_element(self.right_leg_option_xpath)
