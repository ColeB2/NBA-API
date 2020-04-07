import unittest

from api_functions_tests import functions_tests, nba_tests


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(functions_tests, nba_tests)

    unittest.TextTestRunner(verbosity=1).run(suite)
