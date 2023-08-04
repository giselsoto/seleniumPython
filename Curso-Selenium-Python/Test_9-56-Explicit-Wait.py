import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Ver https://selenium-python.readthedocs.io/waits.html#explicit-waits


#SELECCION DE ELEMENTOS POR XPATH
s=Service('C://DriversSelenium/chromedrivert.9.exe')
driver = webdriver.Chrome(service=s)

# Pagina "https://www.seleniumeasy.com/test/" ya no funciona
# Probar con "https://demo.seleniumeasy.com/basic-select-dropdown-demo.html" pero no tiene pop up
# https://www.clarin.com/
# https://www.poptin.com/ (Buscar "pop up pages test")
url='http://the-internet.herokuapp.com/entry_ad'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(10)
t=3 # segundos para el sleep

#Tenemos que ingresar una espera hasta que el elemento sea clickleable
wait = WebDriverWait(driver, 10) #Importado como expected_conditions as EC
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='modal']/div[2]/div[3]/p")))
element.click() #es lo mismo que la proxima linea
#driver.find_element(By.XPATH, "//*[@id='modal']/div[2]/div[3]/p").click()
#Si hacemos hasta aca sin el explicit wait se da este error: "Element <p>...</p> is not clickable at point..."


time.sleep(t)

driver.close()