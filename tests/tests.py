import unittest

from api_functions_tests import functions_tests, nbaboxscore_tests,\
    nbaplayers_tests, nbaschedule_tests, nbascore_tests


if __name__ == '__main__':
    test_modules_to_run = [functions_tests, nbaboxscore_tests, nbaplayers_tests,
        nbaschedule_tests, nbascore_tests]

    loader = unittest.TestLoader()

    suites_list = []
    for test_module in test_modules_to_run:
        suite = loader.loadTestsFromModule(test_module)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner(verbosity=1)
    results = runner.run(big_suite)
