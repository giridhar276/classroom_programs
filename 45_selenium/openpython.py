#Import webdriver module from selenium package
from selenium import webdriver
 
 
driver = webdriver.Chrome()
#Navigate browser to practice.teachmeselenium.com
driver.get("https://www.python.org/")



driver.find_element_by_link_text("Python 3.7.1").click()


driver.implicitly_wait(5)

driver.find_element_by_link_text("Windows x86-64 executable installer").click()
driver.quit()
