from pages.base_page import BasePage


class PlayerPanel(BasePage):

    matches_of_a_player_button_xpath = "//ul[2]/div[2]/div[2]/span"
    add_match_button_xpath = "//a/button/span[1]"

    def click_on_the_matches_of_a_player_button(self):
        self.click_on_the_element(self.matches_of_a_player_button_xpath)

    def click_on_the_add_match_button(self):
        self.click_on_the_element(self.add_match_button_xpath)
