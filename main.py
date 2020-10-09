from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login

username = ''
password = ''
driver = 0

def main():
    global driver
    print('running script')
    driver = webdriver.Chrome('../chromedriver.exe')
    l = login.Login(driver, username, password)
    l.signIn()

if __name__ == '__main__':
    main()
