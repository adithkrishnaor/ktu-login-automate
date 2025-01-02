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
    driver.maximize_window()
    time.sleep(2)
    username = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID,"login-password")

    username.send_keys(username_value)
    password.send_keys(password_value)
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(3)

    #Selecting result button
    resultBtn = driver.find_element(By.XPATH,'//*[@id="7"]')
    resultBtn.click()
    time.sleep(2)

    #Selecting the semester dropdown
    selectSem = driver.find_element(By.XPATH,'//*[@id="semesterGradeCardListingSearchForm_semesterId"]')
    selectSem.click()
    time.sleep(2)

    #Selecting the second semester
    secondSem = driver.find_element(By.XPATH, '//*[@id="semesterGradeCardListingSearchForm_semesterId"]/option[3]')
    secondSem.click()
    time.sleep(2)

    #Selecting the search button
    searchBtn = driver.find_element(By.XPATH,'//*[@id="semesterGradeCardListingSearchForm_search"]')
    searchBtn.click()
    time.sleep(5)

finally:
    driver.quit()