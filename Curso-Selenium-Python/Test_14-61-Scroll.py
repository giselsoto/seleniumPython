import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Ver https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

s=Service('C://DriversSelenium/chromedrivert.9.exe')
driver = webdriver.Chrome(service=s)

url='https://pixabay.com/es/'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(5)
t=3

#driver.execute_script("window.scrollTo(0,1500)")

try:
    descubreMas = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    descubreMas = driver.find_element(By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    #La siguiente funcion da la orden de hacer scroll hasta donde esta el elemento
    ir = driver.execute_script("arguments[0].scrollIntoView();", descubreMas)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(t)
driver.close()