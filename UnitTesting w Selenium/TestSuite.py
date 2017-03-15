import unittest
import HtmlTestRunner
from testCaseTutorial import SearchTest
from multipleTests import HomePageTest

# get all tests from searchTest and HomePageTest classes
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining seach_test and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_test])

# run the suite
unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/DJ/Master/Projects/WorkingSelenium/'))