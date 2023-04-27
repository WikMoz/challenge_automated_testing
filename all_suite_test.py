import unittest

from unittest.loader import makeSuite

from test_cases.adding_a_match import TestAddingAMatch
from test_cases.adding_new_player import TestAddPlayerForm
from test_cases.login_to_the_system import TestLoginPage
from test_cases.searching_players import TestPlayersTable


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestAddPlayerForm))
    test_suite.addTest(makeSuite(TestPlayersTable))
    test_suite.addTest(makeSuite(TestAddingAMatch))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
