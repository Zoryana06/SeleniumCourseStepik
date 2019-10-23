from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "http://SunInJuly.github.io/execute_script.html"
	browser.get(link)
	
	x_element = browser.find_element_by_xpath("//span[@id='input_value']")
	x = x_element.text
	y = calc(x)

	browser.execute_script("window.scrollBy(0, 150);")

	y_element = browser.find_element_by_xpath("//input[@id='answer']")
	y_element.send_keys(y)

	checkbox = browser.find_element_by_xpath("//input[@type='checkbox']").click()
	radiobutton = browser.find_element_by_xpath("//input[@id='robotsRule']").click()

	button = browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	time.sleep(3)
	browser.quit()


