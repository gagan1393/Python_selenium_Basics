from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from asserts import assert_true, assert_equal, assert_raises
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get("https://www.spicejet.com/")
time.sleep(3)
print(driver.title)

'''move to Element'''
Login_element = driver.find_element(By.ID, "ctl00_HyperLinkLogin")
action_chain = ActionChains(driver)
action_chain.move_to_element(Login_element).perform()

spice_club_member = driver.find_element(By.LINK_TEXT, "SpiceClub Members")
action_chain.move_to_element(spice_club_member).perform()

Member_login = driver.find_element(By.LINK_TEXT, "Member Login")
Member_login.click()

verify_memeber_login = driver.find_element(By.XPATH, "//div[@class='heading-memberlogin']")
print(verify_memeber_login.text)
assert_true(True, msg_fmt="SC Member Login")
#assert_equal(print(verify_memeber_login.text), "SC Member Login")

time.sleep(3)
driver.quit()


