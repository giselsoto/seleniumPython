import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath

#SELECCION DE ELEMENTOS POR XPATH
s=Service('C://DriversSelenium/chromedrivert.9.exe')
driver = webdriver.Chrome(service=s)
url='https://demoqa.com/text-box'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()

#NUEVO TEST 8, el "implicit wait" se pone luego de abrir la ventana, se espera a ver si algun elemento falla
driver.implicitly_wait(10)
#variable de tiempo
t=1

#Espera 3 segundos antes de cerrar la ventana
time.sleep(t)
#Va a buscar el campo "Nombre" por XPath
nombre=driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")

#Le enviamos texto
nombre.send_keys("Rodrigo")
time.sleep(t)

email=driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]").send_keys("rodrigo@gmail.com")
time.sleep(t)

direccion1=driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("Casat")
time.sleep(t)

direccion2=driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("Casa2")
time.sleep(t)

#Hay que dar scroll antes para que el banner no tape el boton, porque sino podria dar un error
driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

botonSubmit=driver.find_element(By.XPATH, "//button[contains(@id,'submit')]").click()
time.sleep(3)

driver.close()