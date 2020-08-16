from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from asserts import assert_true, assert_equal, assert_raises
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
driver.maximize_window()
driver.get('https://www.reddit.com/')
#driver.get_screenshot_as_file('reddit.png')

'''full screenshot'''
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME, "body").screenshot('Reddit_Full_Page1.png')

driver.quit()