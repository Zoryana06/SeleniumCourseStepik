from selenium import webdriver
import time
import math

try:
	link = "http://suninjuly.github.io/wait1.html"
	
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get(link)

	button = browser.find_element_by_xpath("//button[@id='verify']").click()

	message = browser.find_element_by_xpath("//div[@id='verify_message']")

	assert "successful" in message.text

finally:
	time.sleep(2)
	browser.quit()
