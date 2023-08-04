# Importo la libreria de selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service(r"C:\chromedriver.exe")

# ubicacion del driver de chrome
driver=webdriver.Chrome(executable_path="C:\DriversSelenium\chromedriver.exe")

# URL que queremos visitar
driver.get("https://demoqa.com/text-box")

print(driver.title)  # Imprime el titulo
driver.close()
