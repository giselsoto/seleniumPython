import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Ver https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

#SELECCION DE ELEMENTOS POR XPATH
s=Service('C://DriversSelenium/chromedrivert.9.exe')
driver = webdriver.Chrome(service=s)

# Pagina "https://www.seleniumeasy.com/test/" ya no funciona
url='https://demoqa.com/select-menu'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(5)
t=1
#Hay que dar scroll
driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

try:
# Vamos a seleccionar en el menu "Old Style Select Menu"
# find Xpath of option: Utilizar Relative xpath!!
    #oldStyleSelect = driver.find_element(By.XPATH, "//select[@id='oldSelectMenu']") #Encontrar el elemento
    oldStyleSelect = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='oldSelectMenu']")))
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
except TimeoutException as ex: #Importar funcion
    print(ex.msg) #Imprime el mensaje de timeout y continua la ejecucion
    print("El elemento no esta disponible")
    #Si no encuentra el elemento (por ejemplo si ponemos mal la url) continua con el bloque siguiente de codigo


#Otra forma mas corta
#Hay que dar scroll
driver.execute_script("window.scrollTo(0,600)")
time.sleep(2)
#Standard multi select
autos = Select(driver.find_element(By.ID, "cars"))
autos.select_by_index(1)
time.sleep(t)

autos.select_by_index(2)
time.sleep(t)

autos.select_by_index(3)
time.sleep(t)

time.sleep(t)

driver.close()