#!/usr/bin/env python

import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from time import sleep


class TestClickEvent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS('phantomjs')
        #self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testStackOverflow(self):
        """This test will go to http://stackoverflow.com/ and click on the Questions nav item"""

        self.driver.get('http://stackoverflow.com/')
        self.assertTrue(u'Stack' in self.driver.page_source, 
                            'Text or page not found')

        #self.assertTrue(self.driver.find_element_by_xpath("//div[@id='hmenus']/div/ul/li/a").is_displayed())
        #self.driver.find_element_by_xpath("//div[@id='hmenus']/div/ul/li/a").click()

        self.assertTrue(self.driver.find_element_by_css_selector("#nav-questions").is_displayed())
        self.driver.find_element_by_css_selector("#nav-questions").click()

        wait = ui.WebDriverWait(self.driver, 5)
        wait.until(lambda driver: u'Questions' in self.driver.page_source,
                                        'Text not in page source')

        current_url = self.driver.current_url
        print "\ncurrent_url is now '%s'" % current_url

if __name__ == '__main__':
    unittest.main()
