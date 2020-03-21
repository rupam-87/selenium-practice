from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
'''driver.get("http://www.python.org")
print(driver.title)
print(driver.current_url)

driver.get("http://www.python.org")

print(driver.title)
driver.get("https://www.glassdoor.co.in/index.htm")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)



driver.forward()'''

driver.get("http://newtours.demoaut.com/")
user=driver.find_element_by_name("userName")
print(user.is_displayed())
print(user.is_enabled())
pas=driver.find_element_by_name("password")
user.send_keys("mercury")
pas.send_keys("mercury")
driver.find_element_by_name("login").click()
check=driver.find_elements_by_css_selector("input[value=roundtrip]")
print(check.is_selected())










