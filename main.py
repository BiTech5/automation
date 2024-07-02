import selenium
from selenium import webdriver
path="c:\\Program Files (x86)\\chromedriver.exe"
driver=webdriver.Chrome(path)
url=r"https://github.com/BiTech5"
driver.get(url)
# for closing the tab
print(driver.title)
driver.quit()


# for closing the browser
# driver.quit()