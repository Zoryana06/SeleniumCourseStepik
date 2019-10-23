from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_xpath("//span[@id='input_value']")
	x = x_element.text
	y = calc(x)
	y_element = browser.find_element_by_xpath("//input[@id='answer']")
	y_element.send_keys(y)

	time.sleep(2)

	option_1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
	option_1.click()

	option_2 = browser.find_element_by_css_selector("[value='robots']")
	option_2.click()

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(5)
	browser.quit()

