from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re
 
# Call Firefox browser
driver = webdriver.Chrome()
driver.implicitly_wait(30)
#Load amazon.in site
driver.get("https://www.amazon.in/")
driver.maximize_window()

# In the search box, enter ' data catalog' and search'
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("data catalog")
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()
driver.implicitly_wait(5)                               
print("done")

driver.find_element_by_link_text("Katalog: Landscape v.9").click()
driver.quit()
   
