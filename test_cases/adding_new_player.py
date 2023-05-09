import os
import unittest
import pyautogui

from selenium import webdriver

from pages.add_a_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from test_cases.login_to_the_system import TestLoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerForm(unittest.TestCase):



    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):

        TestLoginPage.test_log_in_to_the_system(self) # use all tests used in method: test_log_in_to_the_system from object TestLoginPage

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()  # click on the add player button (dashboard)

        add_player_form = AddPlayerForm(self.driver)
        add_player_form.title_of_page()
        add_player_form.type_in_email('player2@gmail.com')
        add_player_form.type_in_name('Player 2')
        add_player_form.type_in_surname('Playerowski')
        add_player_form.type_in_phone('999999999')
        add_player_form.type_in_weight('80')
        add_player_form.type_in_height('190')
        add_player_form.type_in_date_of_birth('31.01.2000')
        add_player_form.click_on_the_leg_select_menu()
        add_player_form.click_on_the_right_leg_option()
        add_player_form.type_in_club('Wild Goats')
        add_player_form.type_in_level('junior')
        add_player_form.type_in_main_position('defender')
        add_player_form.type_in_second_position('midfielder')
        add_player_form.click_on_the_district_select_menu()

        add_player_form.click_on_the_lodz_district_option()

        add_player_form.type_in_achievements('winner of the Winners Cup, 3 goals in 10 seconds')

        var_shot = pyautogui.screenshot()
        var_shot.save('C:/Users/mofyp/GitHub/challenge_automated_testing/TC03-1.png')

        add_player_form.click_on_the_add_language_button()
        add_player_form.type_in_language('english')
        add_player_form.click_on_the_add_language_button()
        add_player_form.type_in_second_language('japanese')
        add_player_form.click_on_the_add_youtube_link_button()
        add_player_form.type_in_youtube_link('https://www.youtube.com/watch?v=gDgFXMKA6QU')
        add_player_form.type_in_facebook_link('https://facebook.com')
        add_player_form.click_on_the_submit_button()


        var_shot = pyautogui.screenshot()
        var_shot.save('C:/Users/mofyp/GitHub/challenge_automated_testing/TC03-2.png')

        add_player_form = AddPlayerForm(self.driver)
        add_player_form.assert_name()
        add_player_form.assert_email()
        add_player_form.assert_surname()
        add_player_form.assert_phone()
        add_player_form.assert_weigt()
        add_player_form.assert_height()
        add_player_form.assert_date_of_birth()
        add_player_form.assert_leg()
        add_player_form.assert_club()
        add_player_form.assert_level()
        add_player_form.assert_main_position()
        add_player_form.assert_second_position()
        add_player_form.assert_district()
        add_player_form.assert_language()
        add_player_form.assert_second_language()
        add_player_form.assert_youtube()
        add_player_form.assert_facebook()

    def test_change_leg(self):
        TestLoginPage.test_log_in_to_the_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()

        add_player_form = AddPlayerForm(self.driver)
        add_player_form.select_leg("right")
        add_player_form.select_leg("left")


