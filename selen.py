import os.path
from selenium import webdriver
driver = webdriver.Firefox()
#reference ；http://stackoverflow.com/questions/8255929/running-webdriver-chrome-with-selenium
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('seleniumhq')
#driver.quit()