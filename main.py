from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import Utilities as utils

#login credentials
username = 'yourusername'
password =  '*************'

#initializing driver
driver = 0 

def main():
    global driver
    print('running script')
    driver = webdriver.Chrome('..//chromedriver.exe')

    l = login.Login(driver, username, password)
    l.signIn() 

    utility = utils.Utilities(driver)

    #If you want to give many likes, you can read a txt file with all the posts links
    """
    links = open('E:/Escritorio/links.txt', 'r')
    for link in links:
        utils.like(link)
    """

    utils.sendMessage('example', 'This is an automated message')

if __name__ == '__main__':
    main()