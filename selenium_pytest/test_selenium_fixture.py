from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("*********************Test Setup****************")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.get("https://www.google.co.in/")

    yield
    print("**************Test Setup completed*******************")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_ggogle_title():
    assert driver.title == "Google"


@pytest.mark.usefixtures("init_driver")
def test_ggogle_URL():
    assert driver.current_url == "https://www.google.co.in/"

