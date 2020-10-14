from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PATH = "F:\hacking\softtesting\chromedriver.exe"
driver = webdriver.Chrome(PATH) 
driver.get("https://www.youtube.com/")
print(driver.title)
search = driver.find_element_by_name("search_query")
search.send_keys("shell")
search.send_keys(Keys.RETURN)
try:
	main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "page-manager")))
	print(main.text)
finally:
	driver.quit()