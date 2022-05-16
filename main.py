from asyncio.windows_events import NULL
from cgitb import text
from ctypes import sizeof
from lib2to3.pgen2.token import EQEQUAL, EQUAL
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

## Driver setting
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://clinico.rayenaps.cl/")

## Login
# Assignation
wait_short = WebDriverWait(driver,20)
wait_long = WebDriverWait(driver,200)

# Algorithm
Ubicacion_input = driver.find_element(By.ID, "location")
Usuario_input = driver.find_element(By.ID, "username")
Clave_input = driver.find_element(By.ID, "password")

Ubicacion_input.clear()
Usuario_input.clear()
Clave_input.clear()

Usuario_input.send_keys("18621997k")
Ubicacion_input.send_keys("csfclotarioblest")
Clave_input.send_keys("1312LKcco")

driver.find_element(By.CLASS_NAME,"btn-secondary").click()

## Menu navegation
# Assignation
wait_short.until(EC.url_contains("main"))

# loading wait
try:
    wait_short.until(EC.presence_of_element_located((By.CLASS_NAME, "cache-loading")))
    wait_long.until_not(EC.presence_of_element_located((By.CLASS_NAME, "cache-loading")))
except:
    pass

# Navegate to list
driver.find_element(By.ID,"navbar-main-menu").click()
driver.find_element(By.XPATH,"//*[contains(text(), 'Box')]").click()
driver.find_element(By.XPATH,"//*[contains(text(), 'Pacientes citados')]").click()

try:
    wait_short.until(EC.presence_of_element_located((By.XPATH,".//*[@id='root']/div/div[1]/div[3]/div[2]/div[3]/div/div/div")))
except:
    pass


print("---------------------------- intento 4 ----------------------------")

print(driver.find_element(By.CSS_SELECTOR,"div.btn-group").text)








#print(driver.find_element(By.XPATH,".//*[@id='root']/div/div/div/div/div/div/div/div").text)
#print(driver.find_element(By.CSS_SELECTOR,"div.rt-tr").text)

# Assertion
## end
