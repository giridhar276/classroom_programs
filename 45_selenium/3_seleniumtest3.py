from selenium import webdriver

import time

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome()

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
driver.find_element_by_class_name('login-email').send_keys("giridhar276@gmail.com")


# sleep for 0.5 seconds
time.sleep(0.5)

# locate password form by_class_name
driver.find_element_by_class_name('login-password').send_keys("ramachandra987")

# send_keys() to simulate key strokes

time.sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()



