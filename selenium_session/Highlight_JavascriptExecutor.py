from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
driver.maximize_window()
driver.get('https://www.amazon.in/')

#form = driver.find_element(By.XPATH, "//form[@id='hs-login']")
#driver.execute_script("arguments[0].style.border = '3px solid red'", form)

Home_products = driver.find_element(By.XPATH, "//span[contains(text(),'Best Sellers in Grocery & Gourmet Foods')]")
driver.execute_script("arguments[0].scrollIntoView(true);", Home_products)