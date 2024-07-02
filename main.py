from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
path="c:\\Program Files (x86)\\chromedriver.exe"
driver=webdriver.Chrome(path)
url=r"https://github.com/BiTech5"
driver.get(url)
search=driver.find_elements(By.TAG_NAME,"h2")
print(search)
print(driver.title)
driver.quit()