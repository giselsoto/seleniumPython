import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Ver https://selenium-python.readthedocs.io/waits.html#explicit-waits


s=Service('C://DriversSelenium/chromedrivert.9.exe')
driver = webdriver.Chrome(service=s)

# Pagina "https://www.seleniumeasy.com/test/" ya no funciona
# Probar con "https://demo.seleniumeasy.com/basic-select-dropdown-demo.html" pero no tiene pop up

#url='https://demoqa.com/checkbox'
url='https://faculty.washington.edu/chudler/java/boxes.html'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(10)
t=4 # segundos para el sleep

#Tenemos que ingresar una espera hasta que el elemento sea clickleable, boton expandir
wait = WebDriverWait(driver, 10) #Importado como expected_conditions as EC
checkbox1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/center[3]/table/tbody/tr/td[1]/form/center/input[2]")))
checkbox1.click() #es lo mismo que la proxima linea
#driver.find_element(By.XPATH, "//*[@id='tree-node']/div/button[1]/svg").click()

checkbox2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/center[3]/table/tbody/tr/td[1]/form/center/input[4]")))
checkbox2.click()

checkbox3 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/center[3]/table/tbody/tr/td[1]/form/center/input[5]")))
checkbox3.click()

time.sleep(t)

driver.close()
