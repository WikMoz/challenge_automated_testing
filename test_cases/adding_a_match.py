import os
import unittest
import time

import pyautogui
from selenium import webdriver

from pages.player_panel import PlayerPanel
from pages.players_table import FilterPlayersTable
from test_cases.searching_players import TestPlayersTable

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddingAMatch(unittest.TestCase):



    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_redirect_to_the_add_match_form(self):

        TestPlayersTable.test_search_a_player(self)

        filter_players_table = FilterPlayersTable(self.driver)
        filter_players_table.click_on_the_player_choosing_button()

        player_panel = PlayerPanel(self.driver)
        player_panel.click_on_the_matches_of_a_player_button()
        player_panel.click_on_the_add_match_button()

        time.sleep(3)

        var_shot = pyautogui.screenshot()
        var_shot.save('C:/Users/mofyp/GitHub/challenge_automated_testing/TC05.png')
