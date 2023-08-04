import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para que funcione By.XPath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Ver https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

s=Service('C://Users/ZF426DY/DriversSelenium/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s)

# https://www.seleniumeasy.com/test/input-form-demo ya no existe
# https://www.techlistic.com/p/selenium-practice-form.html
# https://demoqa.com/automation-practice-form
url='https://demoqa.com/automation-practice-form'
driver.get(url)

# Maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(5)
t=1


# Recargar la página para que no se muestre mas el BANNER
driver.refresh()
# Reducir el nivel de zoom de la página a 75%
#driver.execute_script("document.body.style.zoom='90%'")
#time.sleep(t)

#Vamos a completar los primeros 3 campos
driver.find_element(By.XPATH, "//input[contains(@id,'firstName')]").send_keys("Juan" + Keys.TAB + "Perez" + Keys.TAB + "juan.pereztest@gmail.com")
driver.execute_script("window.scrollTo(0,200)")

#Seleccion de genero
#VER COMO HACERLO CON SELECT
driver.find_element(By.XPATH, "//label[contains(@for,'gender-radio-1')]").click()

#Telefono
driver.find_element(By.XPATH, "//input[contains(@id,'userNumber')]").send_keys("0123456789")

#Fecha
driver.find_element(By.XPATH, "//input[contains(@id,'dateOfBirthInput')]").click()
# Esperar hasta que el date picker esté disponible en el DOM
wait = WebDriverWait(driver, 10)
date_picker_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'react-datepicker')))
# Hay que seleccionar primero el mes, luego el año y al final el dia y con eso se cierra el date-picker
target_month = 'August'
target_year = '2000'
target_day = '30'
# Buscar y seleccionar el mes
month_element = date_picker_popup.find_element(By.XPATH, f"//select[contains(@class,'react-datepicker__month-select')]")
month = Select(month_element)
month.select_by_visible_text(target_month)
time.sleep(t)
# Buscar y seleccionar el año
year_element = date_picker_popup.find_element(By.XPATH, f"//select[contains(@class,'react-datepicker__year-select')]")
year = Select(year_element)
year.select_by_value(target_year)
time.sleep(t)
# Buscar y seleccionar el día
day_element = date_picker_popup.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--0"+target_day+"']")
day_element.click()
time.sleep(t)

#SCROLL
# La siguiente funcion da la orden de hacer scroll hasta donde esta el elemento
try:
    scrollSubmit = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id,'submit')]")))
    scrollSubmit = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", scrollSubmit)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

# Subjects
search_box = driver.find_element(By.XPATH, "//*[@id='subjectsContainer']/div/div[1]")
search_box.click()
time.sleep(t)
# Ingresar caracter
search_input = driver.find_element(By.XPATH, "//*[@id='subjectsInput']")
search_input.send_keys("C")
time.sleep(t)
# Enviar tecla de flecha hacia abajo dos veces para seleccionar la opción deseada
search_input.send_keys(Keys.ARROW_DOWN)
search_input.send_keys(Keys.ARROW_DOWN)
# Enviar tecla Enter para seleccionar la opción deseada
search_input.send_keys(Keys.ENTER)
time.sleep(t)
'''
#Esta forma no funciona porque no puedo seleccionar el elemento para ver el xpath
# Seleccionar la opción deseada (por ejemplo, "Arts")
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-3-option-3']")))
option.click()
'''

#HOBBIES
driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]/label").click()
driver.find_element(By.XPATH, "//label[contains(@for,'hobbies-checkbox-2')]").click()
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3'][contains(.,'Music')]").click()
time.sleep(t)

#PICTURE
try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'uploadPicture')]")))
    buscar = driver.find_element(By.XPATH, "//input[contains(@id,'uploadPicture')]")
    #En la url del archivo hay que poner las barras para el lado opuesto y dobles ("C:\Users\gisel.soto\PycharmProjects\Curso-Selenium-Python\Imagenes\Roque.jpeg")
    buscar.send_keys("C://Users//ZF426DY//PyCharm_Workspace//Curso-Selenium-Python//Imagenes//Roque.jpeg")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")
time.sleep(t)


#CURRENT ADDRESS
driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("MI CASA")
time.sleep(t)


#STATE
#ERROR! SELECT NO FUNCIONA CON DIV Y SVG
# Hacer clic en el campo de búsqueda de Estado para abrir el menú desplegable
# Esperar hasta que el campo de búsqueda de Estado sea interactuable
state_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class=' css-1hwfws3'][contains(.,'Select State')]")))
state_select = driver.find_element(By.XPATH, "//div[@class=' css-1hwfws3'][contains(.,'Select State')]").click()

# Esperar a que aparezcan las opciones filtradas
stateInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class=' css-1wa3eu0-placeholder'][contains(.,'Select State')]")))
#Este Xpath es del cursor, OJO porque cuesta seleccionarlo
stateInputCursor = driver.find_element(By.XPATH, "//*[@id='react-select-3-input']")
stateInputCursor.send_keys("N")
time.sleep(t)
stateInputCursor.send_keys(Keys.ARROW_DOWN)
time.sleep(t)
stateInputCursor.send_keys(Keys.ENTER)

#CITY
# Esperar hasta que el campo de búsqueda de Ciudad sea interactuable
city_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class=' css-1hwfws3'][contains(.,'Select City')]"))).click()

# Esperar a que aparezcan las opciones filtradas
cityInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='city']/div/div[1]")))
#Este Xpath es del cursor, OJO porque cuesta seleccionarlo
cityInputCursor = driver.find_element(By.XPATH, "//*[@id='react-select-4-input']")
time.sleep(t)
cityInputCursor.send_keys(Keys.ARROW_DOWN)
time.sleep(t)
stateInputCursor.send_keys(Keys.ENTER)
#Al dar ENTER es como dar click en boton "Submit"
time.sleep(t)

#Cerrar MODAL
#SCROLL para pantalla pequeña
# La siguiente funcion da la orden de hacer scroll hasta donde esta el elemento
try:
    scrollClose = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id,'closeLargeModal')]")))
    scrollClose = driver.find_element(By.XPATH, "//button[contains(@id,'closeLargeModal')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", scrollClose)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

driver.find_element(By.XPATH, "//button[contains(@id,'closeLargeModal')]").click()
time.sleep(t)
driver.close()

