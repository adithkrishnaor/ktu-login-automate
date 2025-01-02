from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time 

from dotenv import load_dotenv
import os

load_dotenv()

username_value = os.getenv('LOGIN_USERNAME')
password_value = os.getenv('LOGIN_PASSWORD')

driver = webdriver.Chrome()

try:
    driver.get("https://app.ktu.edu.in/login.htm")
    time.sleep(2)
    username = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID,"login-password")

    username.send_keys(username_value)
    password.send_keys(password_value)
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)

finally:
    driver.quit()