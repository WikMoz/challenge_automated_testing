import time

from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    add_player_form_url = "https://scouts.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    email_field_xpath = "//div[2]/div/div[1]/div/div/input"
    expected_email = "player2@gmail.com"
    name_field_xpath = "//div[2]/div/div[2]/div/div/input"
    expected_name = "Player 2"
    surname_field_xpath = "//div[2]/div/div[3]/div/div/input"
    expected_surname = "Playerowski"
    phone_field_xpath = "//div[4]/div/div/input"
    expected_phone_number = "999999999"
    weight_field_xpath = "//div[5]/div/div/input"
    expected_weight = "80"
    height_field_xpath = "//div[6]/div/div/input"
    expected_height = "190"
    date_of_birth_field_xpath = "//div[7]/div/div/input"
    expected_date_of_birth = '2000-01-31'
    leg_select_menu_xpath = '//*[@id="mui-component-select-leg"]'
    right_leg_option_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    left_leg_option_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    expected_leg = "Right"
    club_field_xpath = "//div[9]/div/div/input"
    expected_club = "Wild Goats"
    level_field_xpath = "//div[10]/div/div/input"
    expected_level = "junior"
    main_position_field_xpath = "//div[11]/div/div/input"
    expected_main_position = "defender"
    second_position_field_xpath = "//div[12]/div/div/input"
    expected_second_position = "midfielder"
    district_select_menu_field_xpath = "//*[@id='mui-component-select-district']"
    lodz_district_option_xpath = "//div[3]/ul/li[5]"
    expected_district = "Łódź"
    achievements_field_xpath = "//div[14]/div/div/input"
    expected_achievements = "winner of the Winners Cup, 3 goals in 10 seconds"
    add_language_button_xpath = "//div[15]/button/span[1]"
    language_field_xpath = "//div[15]/div/div/div/input"
    expected_language = "english"
    second_language_field_xpath = "//div[15]/div[2]/div/div/input"
    expected_second_language = "japanese"
    add_youtube_link_button_xpath = "//div[19]/button/span[1]"
    expected_youtube_link = "https://www.youtube.com/watch?v=gDgFXMKA6QU"
    youtube_field_xpath = "//*[@name='webYT[0]']"
    facebook_field_xpath = "//div[18]/div/div/input"
    expected_facebook_link = "https://facebook.com"
    submit_button_xpath = "//div[3]/button[1]/span[1]"
    edit_player_title_xpath = "//form/div[1]/div/span"

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
        self.wait_for_element_to_be_clickable(self.right_leg_option_xpath)
        self.click_on_the_element(self.right_leg_option_xpath)

    def type_in_club(self, club_name):
        self.field_send_keys(self.club_field_xpath, club_name)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def click_on_the_district_select_menu(self):
        self.click_on_the_element(self.district_select_menu_field_xpath)

    def click_on_the_lodz_district_option(self):
        self.wait_for_element_to_be_clickable(self.lodz_district_option_xpath)
        self.click_on_the_element(self.lodz_district_option_xpath)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def click_on_the_add_language_button(self):
        self.click_on_the_element(self.add_language_button_xpath)

    def type_in_language(self, language):
        self.field_send_keys(self.language_field_xpath, language)

    def type_in_second_language(self, language):
        self.field_send_keys(self.second_language_field_xpath, language)

    def click_on_the_add_youtube_link_button(self):
        self.click_on_the_element(self. add_youtube_link_button_xpath)

    def type_in_youtube_link(self, link):
        self.field_send_keys(self.youtube_field_xpath, link)

    def type_in_facebook_link(self, link):
        self.field_send_keys(self.facebook_field_xpath, link)

    def click_on_the_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self. submit_button_xpath)

    def select_leg(self, leg):
        self.click_on_the_element(self.leg_select_menu_xpath)
        if leg == "right":
            self.click_on_the_element(self.right_leg_option_xpath)
        else:
            self.click_on_the_element(self.left_leg_option_xpath)

    def assert_name (self):
        self.longer_wait_for_element_to_be_clickable(self.name_field_xpath)
        self.assert_element_text(self.driver, self.name_field_xpath, self.expected_name)

    def assert_surname(self):
        self.assert_element_text(self.driver, self.surname_field_xpath, self.expected_surname)

    def assert_email(self):
        self.assert_element_text(self.driver, self.email_field_xpath, self.expected_email)

    def assert_phone(self):
        self.assert_element_text(self.driver, self.phone_field_xpath, self.expected_phone_number)

    def assert_weight(self):
        self.assert_element_text(self.driver, self.weight_field_xpath, self.expected_weight)

    def assert_height(self):
        self.assert_element_text(self.driver, self.height_field_xpath, self.expected_height)

    def assert_date_of_birth(self):
        self.assert_element_text(self.driver, self.date_of_birth_field_xpath, self.expected_date_of_birth)

    def assert_leg(self):
        self.assert_element_text(self.driver, self.leg_select_menu_xpath, self.expected_leg)

    def assert_club(self):
        self.assert_element_text(self.driver, self.club_field_xpath, self.expected_club)

    def assert_level(self):
        self.assert_element_text(self.driver, self.level_field_xpath, self.expected_level)

    def assert_main_position(self):
        self.assert_element_text(self.driver, self.main_position_field_xpath, self.expected_main_position)

    def assert_second_position(self):
        self.assert_element_text(self.driver, self.second_position_field_xpath, self.expected_second_position)

    def assert_district(self):
        self.assert_element_text(self.driver, self.lodz_district_option_xpath, self.expected_district)

    def assert_achievements(self):
        self.assert_element_text(self.driver, self.achievements_field_xpath, self.expected_achievements)

    def assert_language(self):
        self.assert_element_text(self.driver, self.language_field_xpath, self.expected_language)

    def assert_second_language(self):
        self.assert_element_text(self.driver, self.second_language_field_xpath, self.expected_second_language)

    def assert_youtube(self):
        self.assert_element_text(self.driver, self.youtube_field_xpath, self.expected_youtube_link)

    def assert_facebook(self):
        self.assert_element_text(self.driver, self.facebook_field_xpath, self.expected_facebook_link)

