import unittest
from tests_12_3 import RunnerTest, TournamentTest


test_suite = unittest.TestSuite()

test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(test_suite)
