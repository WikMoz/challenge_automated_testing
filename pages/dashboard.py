from pages.base_page import BasePage


class Dashboard(BasePage):

    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*[contains(@class,'jss29 jss31')]//child::span"
    select_language_button_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    dev_team_contact_hyperlink_xpath = "//div[3]/a/span[1]"
    add_player_button_xpath = "//*[@href='/pl/players/add']//child::span[1]"
    last_created_player_hyperlink_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_hyperlink_xpath = "//a[2]/button/span[1]"
    last_created_match_hyperlink_xpath = "//a[3]/button/span[1]"
    last_updated_match_hyperlink_xpath = "//a[4]/button/span[1]"
    last_updated_report_hyperlink_xpath = "//a[5]/button/span[1]"


pass
