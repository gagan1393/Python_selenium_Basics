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
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
driver.find_element(By.NAME, 'upfile').send_keys('C:\\Users\\Lenovo\\Desktop\\pythonTesting.txt')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
verify_file = driver.find_element(By.XPATH, "//p[contains(text(),'Your notes on the file we')]").text
print(verify_file)
assert_equal(verify_file, "You've uploaded a file. Your notes on the file were:")

driver.quit()