import os
import unittest
import time
from selenium import webdriver

from pages.add_a_player import AddPlayerForm
from pages.dashboard import Dashboard
from pages.login_page import LoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class TestAddPlayerForm(unittest.TestCase):

   @classmethod
   def setUp(self):
       os.chmod(DRIVER_PATH, 755)
       self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
       self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
       self.driver.fullscreen_window()
       self.driver.implicitly_wait(IMPLICITLY_WAIT)

   def test_add_a_player(self):
       user_login = LoginPage(self.driver)
       user_login.type_in_email('user07@getnada.com')  # enter "user07getnada@com" in the email field
       user_login.type_in_password('Test-1234')  # enter "Test-1234' in the password field
       user_login.click_on_the_sign_in_button()  # click on the sign in button

       time.sleep(2)

       dashboard_page = Dashboard(self.driver)
       dashboard_page.click_on_the_add_player_button()  # click on the add player button (dashboard)

       time.sleep(2)

       add_player_form = AddPlayerForm(self.driver)
       add_player_form.title_of_page()
       add_player_form.type_in_email('player1@gmail.com')
       add_player_form.type_in_name('Player 1')
       add_player_form.type_in_surname('Playerowski')
       add_player_form.type_in_phone('999999999')
       add_player_form.type_in_weight('999999999')
       add_player_form.type_in_height('99999999')
       add_player_form.type_in_date_of_birth('31.01.2025')
       add_player_form.click_on_the_leg_select_menu()
       add_player_form.click_on_the_right_leg_option()



       time.sleep(7)

   @classmethod
   def tearDown(self):
       self.driver.quit()