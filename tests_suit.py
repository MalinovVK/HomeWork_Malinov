import unittest
import test_2
from tests import testing

Test_test_2 = unittest.TestSuite()
Test_test_2.addTest(unittest.TestLoader().loadTestsFromTestCase(test_2.TournamentTest))
run_test_2 = unittest.TextTestRunner(verbosity=2)
run_test_2.run(Test_test_2)

Test_testing = unittest.TestSuite()
Test_testing.addTest(unittest.TestLoader().loadTestsFromTestCase(testing.RunnerTest))
run_testing = unittest.TextTestRunner(verbosity=2)
run_testing.run(Test_testing)
