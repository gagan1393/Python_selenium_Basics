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
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.title
signin_button = driver.find_element(By.NAME, "proceed")
signin_button.click()
time.sleep(2)

alert = driver.switch_to.alert
print(alert.text)
#alert.accept()
alert.dismiss()

driver.switch_to.default_content()

driver.quit()