import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testing(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_navigationBar(self):
        url = "https://sia0.github.io/Apni-Dukaan/stationery.html"
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "Offers").click()
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) > .nav-link").click()
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "FAQ").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Mobile").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "TV/Appliances").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Furniture").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Baby/Kids").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Login/Signup").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Stationery").click()


