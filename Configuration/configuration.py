from selenium import webdriver
import unittest

class SeleniumDriver(unittest.TestCase):
        baseUrl = "https://www.ebay.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)


