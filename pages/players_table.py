from pages.base_page import BasePage


class FilterPlayersTable(BasePage):
    players_table_url = "https://scouts-test.futbolkolektyw.pl/pl/players"
    filter_table_button_xpath = "//*[@data-testid = 'Filter Table-iconButton']"
    filter_name_field_xpath = "//div[1]/div/div/div/input"
    filter_surname_field_xpath = "//div[2]/div/div/div/input"
    filter_min_age_field_xpath = "//div[3]/div/div/div/div[1]/div/input"
    filter_max_age_field_xpath = "//div[3]/div/div/div/div[2]/div/input"
    filter_main_position_field_xpath = "//div[4]/div/div/div/input"
    filter_club_field_xpath = "//div[5]/div/div/div/input"
    filter_min_rate_field_xpath = "//div[6]/div/div/div/div[1]/div/input"
    filter_max_rate_field_xpath = "//div[6]/div/div/div/div[2]/div/input"
    title_filters_xpath = "//div[3]/div/div[1]/div[1]/p"
    filter_reset_button_xpath = "//div[1]/div[1]/button/span[1]"
    filter_closing_button_xpath = "//div[3]/button"
    searched_name_xpath = "//td[1]/div[2]"
    expected_name_title = "Player 4"
    searched_surname_xpath = "//td[2]/div[2]"
    expected_surname_title = "Playerowski"
    searched_age_xpath = "//td[3]/div[2]"
    expected_age_title = "23"
    searched_main_position_xpath = "//td[4]/div[2]"
    expected_main_position_title = "defender"
    searched_club_xpath = "//td[5]/div[2]"
    expected_club_title = "Wild Goats"

    def click_on_the_filter_table_button(self):
        self.click_on_the_element(self.filter_table_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.filter_name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.filter_surname_field_xpath, surname)

    def type_in_age_min(self, age_min):
        self.field_send_keys(self.filter_min_age_field_xpath, age_min)

    def type_in_age_max(self, age_max):
        self.field_send_keys(self.filter_max_age_field_xpath, age_max)

    def type_in_main_position(self, position):
        self.field_send_keys(self.filter_main_position_field_xpath, position)

    def type_in_club(self, club):
        self.field_send_keys(self.filter_club_field_xpath, club)

    def type_in_rate_min(self, rate_min):
        self.field_send_keys(self.filter_name_field_xpath, rate_min)

    def type_in_rate_max(self, rate_max):
        self.field_send_keys(self.filter_max_rate_field_xpath, rate_max)

    def click_on_the_closing_button(self):
        self.click_on_the_element(self.filter_closing_button_xpath)

    def searched_name(self):
        self.assert_element_text(self.driver, self.searched_name_xpath, self.expected_name_title)

    def searched_surname(self):
        self.assert_element_text(self.driver, self.searched_surname_xpath, self.expected_surname_title)

    def searched_age(self):
        self.assert_element_text(self.driver, self.searched_age_xpath, self.expected_age_title)

    def searched_club(self):
        self.assert_element_text(self.driver, self.searched_club_xpath, self.expected_club_title)

    def searched_main_position(self):
        self.assert_element_text(self.driver, self.searched_main_position_xpath, self.expected_main_position_title)
