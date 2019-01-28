#Import webdriver module from selenium package
from selenium import webdriver
 
 
driver = webdriver.Chrome()
#Navigate browser to practice.teachmeselenium.com
driver.get("https://www.google.com")



driver.find_element_by_link_text("Images").click()


driver.implicitly_wait(5)

driver.find_element_by_link_text("Gmail").click()
driver.quit()
