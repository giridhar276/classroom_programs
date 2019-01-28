from selenium import webdriver
 
 
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")

driver.get_screenshot_as_file("abcde.png")