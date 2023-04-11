from pages.base_page import BasePage


class Dashboard(BasePage):

    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    select_language_button_xpath = "//div[@class='MuiListItemText-root']//child::span"
    sign_out_button_xpath = "//span[text()='Sign out']"
    dev_team_contact_hyperlink_xpath = "//span[text()='Dev team contact']"
    add_player_button_xpath = "//span[text()='Add player']"
    last_created_player_hyperlink_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_hyperlink_xpath = "//a[2]/button/span[1]"
    last_created_match_hyperlink_xpath = "//a[3]/button/span[1]"
    last_updated_match_hyperlink_xpath = "//a[4]/button/span[1]"
    last_updated_report_hyperlink_xpath = "//a[5]/button/span[1]"


pass
