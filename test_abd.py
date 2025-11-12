import pytest
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

def setup_function():
    global driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://alnafi.com/auth/sign-in")
    driver.maximize_window()

def teardown_function():
    driver.quit()

def my_cred():
    return [
        ('abdeali@gmail.com', 'abd@123'),
        ('abd@gmail.com', 'abd@123'),
        ('ali@gmail.com', 'abd@123')
    ]

@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("my pytest login")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys(username)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[2]/div/div/input').send_keys(password)
    time.sleep(1)
    allure.attach(driver.get_full_page_screenshot_as_png(),name="myalnafi_sc",attachment_type=AttachmentType.PNG)