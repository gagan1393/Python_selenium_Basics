from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
time.sleep(3)

drag_source = driver.find_element(By.ID, "draggable")
drop_destination = driver.find_element(By.ID, "droppable")

act_chains = ActionChains(driver)
#act_chains.drag_and_drop(drag_source, drop_destination).perform()

act_chains\
    .click_and_hold(drag_source)\
    .move_to_element(drop_destination)\
    .release()\
    .perform()

driver.quit()
