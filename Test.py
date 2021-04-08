from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("test case started")
driver = webdriver.Chrome(r"C:\Users\E402B\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.gmail.com")
driver.find_element_by_id("identifierId").send_keys("nurmimisyaheeda@gmail.com")
time.sleep(2)
driver.find_element_by_xpath("//span[@class='VfPpkd-vQzf8d'][1]").click()
time.sleep(3)
driver.find_element_by_name("password").send_keys("Umengohyeah10..")
time.sleep(3)
driver.find_element_by_xpath("//span[contains(text(),'Next')][1]").click()
time.sleep(3)
driver.close()
print("Gmail login has been successfully completed")
