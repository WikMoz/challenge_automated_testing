import os
import unittest
import time
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.players_table import FilterPlayersTable
from test_cases.login_to_the_system import TestLoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestPlayersTable(unittest.TestCase):



    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_search_a_player(self):

        TestLoginPage.test_log_in_to_the_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_players_button()

        filter_players_table = FilterPlayersTable(self.driver)
        filter_players_table.click_on_the_filter_table_button()
        filter_players_table.type_in_name('Player 4')
        filter_players_table.type_in_surname('Playerowski')
        filter_players_table.type_in_club('Wild Goats')
        filter_players_table.type_in_main_position('defender')
        filter_players_table.type_in_age_min('20')
        filter_players_table.type_in_age_max('24')
        time.sleep(3)
        filter_players_table.click_on_the_closing_button()
        time.sleep(3)
        filter_players_table.searched_name()
        filter_players_table.searched_surname()
        filter_players_table.searched_age()
        filter_players_table.searched_club()
        filter_players_table.searched_main_position()



