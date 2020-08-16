from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest
import unittest

class TestMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(20)
        cls.driver.get("https://app.hubspot.com/login")

    def test_login(self):
        self.driver.find_element(By.ID, 'username').clear()
        self.driver.find_element(By.ID, 'username').send_keys("Helloword@gmail.com")
        self.driver.find_element(By.ID, 'password').clear()
        self.driver.find_element(By.ID, 'password').send_keys("Helloword12222")
        self.driver.find_element(By.ID, 'loginBtn').click()

    def test_login2(self):
        self.driver.find_element(By.ID, 'username').clear()
        self.driver.find_element(By.ID, 'username').send_keys("Helloword@rediffcom")
        self.driver.find_element(By.ID, 'password').clear()
        self.driver.find_element(By.ID, 'password').send_keys("kklnbvh12222")
        self.driver.find_element(By.ID, 'loginBtn').click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()






