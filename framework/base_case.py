from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
from framework.config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from framework.elements import *


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        global wait
        global base_url

        base_url = Config.base_url
        if sys.platform == 'darwin':
            driver = webdriver.Chrome()
        if sys.platform == 'win32':
            driver = webdriver.Chrome('lib/chromedriver.exe')

        driver.get(base_url+'index.html')
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)

    @classmethod
    def tearDownClass(cls):
        """ Quite the browser """
        driver.quit()

    def wait_until_element_clickable(self, locator):

        element = None
        if locator[0] == 'xpath':
            element = wait.until(EC.element_to_be_clickable((By.XPATH, locator[1])))
        elif locator[0] == 'id':
            element = wait.until(EC.element_to_be_clickable((By.ID, locator[1])))
        elif locator[0] == 'name':
            element = wait.until(EC.element_to_be_clickable((By.NAME, locator[1])))
        elif locator[0] == 'CSS Selector':
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator[1])))
        return element

    def wait_for_element_visibility(self, locator):
        element = None
        if locator[0] == 'xpath':
            element = wait.until(EC.visibility_of_element_located((By.XPATH, locator[1])))
        elif locator[0] == 'id':
            element = wait.until(EC.visibility_of_element_located((By.ID, locator[1])))
        elif locator[0] == 'name':
            element = wait.until(EC.visibility_of_element_located((By.NAME, locator[1])))
        elif locator[0] == 'CSS Selector':
            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator[1])))
        return element

    def Click(self, locator):
        """ Click the specifies element """
        element = self.wait_until_element_clickable(locator)
        element.click()

    def Clear(self, locator):
        """ Click the specifies element """
        element = self.wait_until_element_clickable(locator)
        element.clear()

    def Send(self, locator, txt):
        """ Send the text to the specifies element/field """
        element = self.wait_until_element_clickable(locator)
        element.click()
        element.clear()
        element.send_keys(txt)

    def FilloutFilled(self, locator, txt):
        """ Send the text to the specifies element/field """
        element = self.wait_until_element_clickable(locator)
        element.click()
        element.clear()
        element.send_keys(txt)

    def Select(self, locator, txt):
        """ Send the text  to the dropdown field - this will select the specifies item"""
        element = self.wait_until_element_clickable(locator)
        element.send_keys(txt)

    def Open(self, url):
        """ Navigates the current browser window to the specified page. """
        driver.get(url)
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        except TimeoutError:
            print("Loading took too much time!")

    def Navigate(self, locator):
        """ Navigates the current browser window to the page using the specified menu item. """
        element = self.wait_until_element_clickable(locator)
        element.click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        except TimeoutError:
            print("Loading took too much time!")

    def get_page_source(self):
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="myTable_x"]/table/tbody/tr[1]')))

        p_source = driver.page_source

        return p_source

