from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C://DriversSelenium/chromedriver1.9.exe')
driver = webdriver.Chrome(service=s)
url='https://demoqa.com/text-box'
driver.get(url)
print("Bienvenido a Selenium")
print(driver.title)
driver.close()
