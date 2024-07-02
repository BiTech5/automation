import selenium
from selenium import webdriver
path="c:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://google.com")