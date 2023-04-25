from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    my_team_input_xpath = "//input[@name='myTeam']"
    enemy_team_input_xpath = "//input[@name='enemyTeam']"
    my_team_score_input_xpath = "//div[3]/div/div/input"
    enemy_team_score_input_xpath = "//input[@name='enemyTeamScore']"
    date_input_xpath = "//input[@name='date']"
    match_at_home_option_xpath = "//input[@type='radio' and @value='true']"
    match_out_home_option_xpath = "//input[@type='radio' and @value='false']"
    tshirt_color_input_xpath = "//input[@name='tshirt']"
    league_input_xpath = "//div[8]/div/div/input"
    time_played_input_xpath = "//div[9]/div/div/input"
    number_input_xpath = "//input[contains(@name,'number')]"
    web_match_input_xpath = "//div[11]/div/div/input"
    add_a_match_form_url = "https://www.scouts-test.futbolkolektyw.pl/en/players/6447e5147ccfb69252f31418/matches/add"
    expected_title = "Adding match player Player 4 Playerowski"


    def wait_for_element(self):
        self.wait_for_element_to_be_clickable(self.my_team_input_xpath)

