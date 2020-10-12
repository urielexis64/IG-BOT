from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Login:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password
    
    def signIn(self):
        #Open Instagram website
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/')

        #locate Username input text
        uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
        uid.click()
        uid.send_keys(self.username)

        #locate Password input text
        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')))
        password.click()
        password.send_keys(self.password)

        #locate and click Login button
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button')))
        button.click()
        time.sleep(5)