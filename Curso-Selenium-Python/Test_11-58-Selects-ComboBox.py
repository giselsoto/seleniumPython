import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Ver https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.support.ui import Select

#SELECCION DE ELEMENTOS POR XPATH
s=Service('C://DriversSelenium/chromedrivert.9.exe')
driver = webdriver.Chrome(service=s)

# Pagina "https://www.seleniumeasy.com/test/" ya no funciona

url='https://demoqa.com/select-menu'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(5)
t=2


#Hay que dar scroll
driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

# Vamos a seleccionar en el menu "Old Style Select Menu"
# find Xpath of option: Utilizar Relative xpath!!
oldStyleSelect = driver.find_element(By.XPATH, "//select[@id='oldSelectMenu']") #Encontrar el elemento
oS = Select(oldStyleSelect)
# select by visible text, el menos confiable
oS.select_by_visible_text("Red")
time.sleep(t)

#Seleccionar por indice es mejor ya que el texto puede variar
oS.select_by_index(2)
time.sleep(t)

#Seleccionar por Value: Ver en inspeccionar y desplegar para ver los values, en este caso es el numero en lugar del texto
oS.select_by_value("8")
time.sleep(t)

#Hay que dar scroll
driver.execute_script("window.scrollTo(0,600)")
time.sleep(2)

#Standard multi select
#Otra forma mas corta
autos = Select(driver.find_element(By.ID, "cars"))
autos.select_by_index(1)
time.sleep(t)

autos.select_by_index(2)
time.sleep(t)

autos.select_by_index(3)
time.sleep(t)

time.sleep(t)

driver.close()