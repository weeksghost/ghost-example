#!/usr/bin/env python

import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui

class TestClickEvent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS('phantomjs')

    def tearDown(self):
        self.driver.quit()

    def testClick(self):
        """Simple Google search for python"""

        self.driver.get('http://www.google.com')
        self.assertTrue(u'Google' in self.driver.page_source, 
                            'Text or page not found')

        self.assertTrue(self.driver.find_element_by_name("q").is_displayed())
        xpath = self.driver.find_element_by_xpath("gbqfq")
        xpath.send_keys("python")

        wait = ui.WebDriverWait(self.driver, 5)
        wait.until(lambda driver: u'python' in self.driver.page_source,
                                        'Text not in page source')

        current_url = self.driver.current_url
        print("\ncurrent_url is now '%s'" % current_url

if __name__ = '__main__':
    unittest.main()
