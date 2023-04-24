from pages.base_page import BasePage


class PlayersTable(BasePage):
    players_table_url = "https://scouts-test.futbolkolektyw.pl/pl/players"
    filter_table_button_xpath = "/*[@data-testid = 'Filter Table-iconButton']"
    filter_name_field_xpath = "//div[1]/div/div/div/input"
    filter_surname_field_xpath = "//div[2]/div/div/div/input"
    filter_min_age_field_xpath = "//div[3]/div/div/div/div[1]/div/input"
    filter_max_age_field_xpath = "//div[3]/div/div/div/div[2]/div/input"
    filter_main_position_field_xpath = "//div[4]/div/div/div/input"
    filter_club_field_xpath = "//div[5]/div/div/div/input"
    filter_min_rate_field_xpath = "//div[6]/div/div/div/div[1]/div/input"
    