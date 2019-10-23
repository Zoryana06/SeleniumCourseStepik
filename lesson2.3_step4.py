from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/alert_accept.html"
	browser.get(link)
	
	button = browser.find_element_by_xpath("//button[@type='submit']").click()

	alert = browser.switch_to.alert
	alert.accept()

	number = browser.find_element_by_xpath("//span[@id='input_value']")
	x = number.text
	y = calc(x)

	element = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)

	button = browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	time.sleep(5)
	browser.quit()
