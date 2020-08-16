from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_page_load_timeout(20)
driver.maximize_window()
driver.get('https://www.amazon.in/')

best_seller = driver.find_element(By.LINK_TEXT, "Best Sellers")
#click the element
driver.execute_script("arguments[0].click();", best_seller)

#get the title of the page
title = driver.execute_script("return document.title;")
print(title)

# Refresh
driver.execute_script("history.go[0];")

#Text in the page
inner_text = driver.execute_script(" return document.documentElement.innerText;")
print(inner_text)

#To highlight the element
driver.execute_script("arguments[0].style.border = '3px solid red'", best_seller)


driver.close()