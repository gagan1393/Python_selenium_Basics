from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)


def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)

select_employee = driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
select_industry = driver.find_element(By.ID, "Form_submitForm_Industry")

select_values(select_employee, "26 - 50")
select_values(select_industry, "Automotive")

time.sleep(2)

