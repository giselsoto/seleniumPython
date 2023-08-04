import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.common.keys import Keys


#SELECCION DE ELEMENTOS POR AND
#Se utiliza @ y comillas simples
s=Service('C://DriversSelenium/chromedrivertiempo.9.exe')
driver = webdriver.Chrome(service=s)

tiempo=3

url='https://demoqa.com/text-box'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
#Espera 3 segundos antes de cerrar la ventana
time.sleep(tiempo)

url2='https://www.selenium.dev/documentation/webdriver/elements/locators/'
driver.get(url2)
time.sleep(tiempo)

url3='https://codegrepper.com/code-examples/python/selenium+send+enter+key'
driver.get(url3)
time.sleep(tiempo)

#Con la siguiente funcion vuelve a la pagina anterior, pero no funciona el contador de tiempo
#driver.back()
#time.sleep(tiempo)

#Con esto controlamos el tiempo el -1 significa que vuelve a la pagina anterior
driver.execute_script("window.history.go(-1)")
time.sleep(tiempo)

driver.execute_script("window.history.go(-1)")
time.sleep(tiempo)

#driver.forward()
driver.execute_script("window.history.go(2)")
time.sleep(tiempo)

driver.close()