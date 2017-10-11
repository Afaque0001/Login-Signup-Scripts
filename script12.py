import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://104.194.229.122:8988")
assert "BitsAuto" in driver.title
elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys("admin")
elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("%%;lX82L|DfpVtQ")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_class_name("item" , value="name")
elem.send_keys(Keys.RETURN)
