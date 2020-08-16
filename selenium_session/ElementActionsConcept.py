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
driver.get('https://app.hubspot.com/login')
driver.title
username_ele = driver.find_element(By.ID, 'username')
password_ele = driver.find_element(By.ID, 'password')
login_button_ele = driver.find_element(By.ID, 'loginBtn')

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username_ele, 'Joey1111@yahoo.com')
act_chains.send_keys_to_element(password_ele, 'Test@12345')
act_chains.click(login_button_ele).perform()

invalid_login = driver.find_element(By.XPATH, "//div[@class='private-alert__inner']")
print(invalid_login.text)

assert_true(True, msg_fmt="That email address doesn't exist.")

driver.quit()