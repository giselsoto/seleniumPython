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

url='https://testpages.herokuapp.com/styled/file-upload-test.html'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(5)
t=1

try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fileinput']")))
    buscar = driver.find_element(By.XPATH, "//input[@id='fileinput']")
    #En la url del archivo hay que poner las barras para el lado opuesto y dobles ("C:\Users\gisel.soto\PycharmProjects\Curso-Selenium-Python\Imagenes\Roque.jpeg")
    buscar.send_keys("C://Users//gisel.soto//PycharmProjects//Curso-Selenium-Python//Imagenes//Roque.jpeg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]").click()
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(t)
driver.close()