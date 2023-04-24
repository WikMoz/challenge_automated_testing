import time

from pages.base_page import BasePage


class Dashboard(BasePage):

    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*[contains(@class,'jss29 jss31')]//child::span"
    select_language_button_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    dev_team_contact_hyperlink_xpath = "//div[3]/a/span[1]"
    add_player_button_xpath = "//div/div/a/button/span[1]"
    last_created_player_hyperlink_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_hyperlink_xpath = "//a[2]/button/span[1]"
    last_created_match_hyperlink_xpath = "//a[3]/button/span[1]"
    last_updated_match_hyperlink_xpath = "//a[4]/button/span[1]"
    last_updated_report_hyperlink_xpath = "//a[5]/button/span[1]"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)
