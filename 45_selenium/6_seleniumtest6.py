from selenium import webdriver
from selenium.webdriver import ActionChains
 
 
driver = webdriver.Chrome()
driver.get("https://www.imdb.com/")
eleMenuShowtimes = driver.find_element_by_id("navTitleMenu")
print(eleMenuShowtimes.text) 
action_chains = ActionChains(driver)
action_chains.move_to_element(eleMenuShowtimes)
action_chains.click(driver.find_element_by_link_text("In Theaters"))
action_chains.perform()
 
if driver.title == "New Movies In Theaters - IMDb":
    print("Passed")
else:
    print("Failed")
 
driver.quit()
