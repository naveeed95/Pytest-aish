import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


Url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
search_menu = ["Admin","PIM", "Leave", "Time","Recruitment","My Info","Performance", "Dashboard","Directory","Maintainance", "Buzz"]
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver

    driver.close()

def test_seach(browser):
    browser.get(Url)
    time.sleep(3)
    browser.find_element(By.NAME, "username").send_keys("Admin")
    time.sleep(3)
    browser.find_element(By.NAME,"password").send_keys("admin123")
    time.sleep(3)
    browser.find_element(By.CLASS_NAME,"oxd-button").click()
    time.sleep(5)
    assert browser.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    time.sleep(3)
    for item in search_menu:
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div").click()
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(item)
        time.sleep(6)
        assert item in browser.page_source
        for i in item:
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACK_SPACE)
        time.sleep(2)
    
