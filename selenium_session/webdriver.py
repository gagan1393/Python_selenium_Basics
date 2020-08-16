from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='D:\\Selenium_software\\driver\\chromedriver.exe')
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
time.sleep(3)
driver.find_element(By.NAME, 'q').send_keys("Naveen AutomationLabs")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(optionsList)
time.sleep(3)

for ele in optionsList:
    print(ele.text)
    if ele.text == 'naveen automationlabs github':
        ele.click()
        break
time.sleep(3)
print(driver.title)
driver.quit()
