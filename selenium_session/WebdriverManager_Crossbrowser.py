from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = "firefox"

if browserName == "chrome":
   driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
   driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
   driver = webdriver.safari()
else:
   print('Please Pass the correct Browser Name :' + browserName)

driver.implicitly_wait(20)
driver.get("https://app.hubspot.com/login")
driver.maximize_window()
driver.find_element(By.ID, 'username').send_keys("Helloword@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Helloword12222")
driver.find_element(By.ID, 'loginBtn').click()

time.sleep(2)

print(driver.title)

driver.quit()

