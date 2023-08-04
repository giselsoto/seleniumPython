import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.common.keys import Keys

#SELECCION DE ELEMENTOS POR AND
#Se utiliza @ y comillas simples
s=Service('C://DriversSelenium/chromedriver1.9.exe')
driver = webdriver.Chrome(service=s)
url='https://demoqa.com/text-box'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
#Espera 3 segundos antes de cerrar la ventana
time.sleep(1)
#Va a buscar el campo "Nombre" por XPath con AND
nombre=driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']")

#Le enviamos texto
nombre.send_keys("Rodrigo")

#Vamos a utilizar KEYS.TAB para hacer un salto de campo, hay que importar "Keys" antes
nombre.send_keys(Keys.TAB + "rodrigo@gmail.com" + Keys.TAB + "Direccion uno" + Keys.TAB + "Direccion dos" + Keys.TAB + Keys.ENTER)
#Asi no funciona, se escribe el mail en el mismo campo del nombre. Hay que concatenar luego del TAB
#nombre.send_keys("rodrigo@gmail.com")

driver.execute_script("window.scrollTo(0,300)")
#Sino puedo usar "Keys.PAGE_DOWN" concatenado arriba
time.sleep(4)
#El elemento "Check Box" no interactua con enter, para esto usamos click
driver.find_element(By.XPATH, "(//span[contains(@class,'text')])[2]").click()
time.sleep(2)

time.sleep(2)






driver.close()