# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://dev.reali.supply/#/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Workplace safety'])[2]/following::span[3]").click()
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Workplace safety'])[2]/following::img[1]").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Workplace safety'])[2]/following::img[1]").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("j.shpylka@softpositive.com")
        driver.find_element_by_id("pwd").click()
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("1qaz2wsx3edc")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Workplace safety'])[2]/following::img[1]").click()
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_link_text("Manage Brands").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[51]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[51]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[51]/following::input[1]").send_keys("test")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[51]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Workplace safety'])[2]/following::img[1]").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
