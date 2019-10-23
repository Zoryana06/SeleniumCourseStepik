from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/selects1.html")

	num_1 = browser.find_element_by_xpath("//span[@id='num1']")
	x = int(num_1.text)
	num_2 = browser.find_element_by_xpath("//span[@id='num2']")
	y = int(num_2.text)
	sum = str(x + y)

	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(sum)

	time.sleep(2)

	button = browser.find_element_by_css_selector("button.btn").click()


finally:
	time.sleep(6)
	browser.quit()	
