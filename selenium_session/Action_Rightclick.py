from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
right_click_ele = driver.find_element(By.XPATH, "//span[text()='right click me']")
act_chain = ActionChains(driver)
act_chain.context_click(right_click_ele).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')
for ele in right_click_options:
    print(ele.text)
    if ele.text == "Delete":
        ele.click()
        break

time.sleep(3)
driver.quit()