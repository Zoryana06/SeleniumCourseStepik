from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	
	browser = webdriver.Chrome()
	browser.get(link)
	
	time.sleep(1)

	button = browser.find_element_by_xpath("//button[@type='submit']").click()

	current_window = browser.window_handles[0]
	window_name = browser.window_handles[1]
	browser.switch_to.window(window_name)

	number = browser.find_element_by_xpath("//span[@id='input_value']")
	x = number.text
	y = calc(x)

	element = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)

	button = browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	time.sleep(5)
	browser.quit()
