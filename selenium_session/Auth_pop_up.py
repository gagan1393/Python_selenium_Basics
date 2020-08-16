from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from asserts import assert_true, assert_equal, assert_raises
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
verify_auth = driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credenti')]").text
print(verify_auth)
assert_equal(verify_auth, "Congratulations! You must have the proper credentials.")

driver.quit()