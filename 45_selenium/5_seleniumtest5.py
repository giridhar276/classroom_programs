from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
import pprint
  
chrome_path = './chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.linkedin.com")
driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="login-email"]""").send_keys("giridhar276@gmail.com")
driver.find_element_by_xpath("""//*[@id="login-password"]""").send_keys("ramachandra987")
driver.find_element_by_xpath("""//*[@id="login-submit"]""").click()
driver.get("https://www.linkedin.com/in/adityaunde/") #Enter any of your connection profile Link
connectionName = driver.find_element_by_class_name('pv-top-card-section__name').get_attribute('innerHTML')
#print(connectionName)

