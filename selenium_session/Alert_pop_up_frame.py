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
driver.get('http://www.londonfreelance.org/courses/frames/index.html')

frame_element = driver.find_element(By.NAME, "main")
driver.switch_to.frame(frame_element)
header = driver.find_element(By.XPATH, "//h2[contains(text(),'Title bar')]").text
print(header)

driver.quit()

