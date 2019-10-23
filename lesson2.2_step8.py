from selenium import webdriver
import os
import time

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/file_input.html"
	browser.get(link)
	
	first_name = browser.find_element_by_xpath("//input[@name='firstname']").send_keys("Zoryana")
	last_name = browser.find_element_by_xpath("//input[@name='lastname']").send_keys("Pokotska")
	email = browser.find_element_by_xpath("//input[@name='email']").send_keys("email@example.com")
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	element = browser.find_element_by_xpath("//input[@type='file']").send_keys(file_path)

	button = browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	time.sleep(5)
	browser.quit()


