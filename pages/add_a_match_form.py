from pages.base_page import BasePage


class add_a_match_form(BasePage):
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
    



