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
driver1 = webdriver.Chrome()

def login():
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
        return driver.title

    finally:
        driver.quit()

def test_login():
    assert login() == "APJ Abdul Kalam Technological University"

def search_result():
    try:
        driver1.get("https://app.ktu.edu.in/login.htm")
        driver1.maximize_window()
        time.sleep(2)
        username = driver1.find_element(By.ID, "login-username")
        password = driver1.find_element(By.ID,"login-password")

        username.send_keys(username_value)
        password.send_keys(password_value)
        time.sleep(2)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

        resultBtn = driver1.find_element(By.XPATH,'//*[@id="7"]')
        resultBtn.click()
        time.sleep(2)

        selectSem = driver1.find_element(By.XPATH,'//*[@id="semesterGradeCardListingSearchForm_semesterId"]')
        selectSem.click()
        time.sleep(2)

        secondSem = driver1.find_element(By.XPATH, '//*[@id="semesterGradeCardListingSearchForm_semesterId"]/option[2]')
        secondSem.click()
        time.sleep(2)

        searchBtn = driver1.find_element(By.XPATH,'//*[@id="semesterGradeCardListingSearchForm_search"]')
        searchBtn.click()
        time.sleep(5)

        res = driver1.find_element(By.XPATH,'//*[@id="page-content-wrapper"]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/h5/strong')
        return res.text
    
    finally:
        driver1.quit()

def test_search_result():
    assert search_result() == "Semester Grade Card"