from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Utilities:
    def __init__(self, driver):
        self.driver = driver

    def like(self, url):
        try:
            self.driver.get(url)

            #locate like button
            uid = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')))
            uid.click()

            #wait for the next action
            time.sleep(3)

        #if the link doesn't exist, we don't do anything
        except:
            pass
    
    def sendMessage(self, user, message):
        try:
            #locate direct messages button
            directMessages = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a')))
            directMessages.click()
            time.sleep(2)

            #locate turn off notifications button
            turnOffNotifications = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')))
            turnOffNotifications.click()
            time.sleep(1)

            #locate new message button
            newMessage = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.oNO81 > div.S-mcP > div > div._2NzhO.EQ1Mr > button')))
            newMessage.click()
            time.sleep(1)
            
            #locate search input
            searchInput = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div.TGYkm > div > div.HeuYH > input')))
            searchInput.click()
            time.sleep(.5)
            searchInput.send_keys(user)
            time.sleep(1)

            #locate first result
            first = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div.Igw0E.IwRSH.eGOV_.vwCYk._3wFWr > div:nth-child(1)')))
            first.click()

            #locate "Next" button
            nextBtn = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > div > button')))
            nextBtn.click()
            time.sleep(2)

            #locate textarea to write the message
            textArea = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea')))
            textArea.click()

            #write and send the message
            textArea.send_keys(message)
            time.sleep(1)
            textArea.send_keys(Keys.ENTER)
            
        except:
            pass
        
        