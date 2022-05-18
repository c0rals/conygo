from asyncio.windows_events import NULL
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import dataExtraction as excel

# Driver setting
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait_short = WebDriverWait(driver, 20)
wait_long = WebDriverWait(driver, 200)

# Login
def login(driver):
    driver.get("https://clinico.rayenaps.cl/")
    Ubicacion_input = driver.find_element(By.ID, "location")
    Usuario_input = driver.find_element(By.ID, "username")
    Clave_input = driver.find_element(By.ID, "password")

    Ubicacion_input.clear()
    Usuario_input.clear()
    Clave_input.clear()

    Usuario_input.send_keys("18621997k")
    Ubicacion_input.send_keys("csfclotarioblest")
    Clave_input.send_keys("1312LKcco")
    driver.find_element(By.CLASS_NAME, "btn-secondary").click()

    wait_short.until(EC.url_contains("main"))

    try:
        wait_short.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "cache-loading")))
        wait_long.until_not(EC.presence_of_element_located(
            (By.CLASS_NAME, "cache-loading")))

        print("[+] Login success")
    except:
        print("[!] Login fail")
        pass
    return driver

# Navegate to list
def goToTable(driver):
    driver.find_element(By.ID, "navbar-main-menu").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Box')]").click()
    driver.find_element(
        By.XPATH, "//*[contains(text(), 'Pacientes citados')]").click()
    try:
        wait_short.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "div.ReactTable.table-height")))
        wait_short.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "div.rt-thead.-header")))
        print("[+] Table load success")
    except:
        print("[!] Table load fail")
        pass
    return driver

# Get list of names (need to be valid names, not all names)
def getNamesFromTable(driver):
    table = driver.find_element(By.CSS_SELECTOR, "div.ReactTable.table-height")
    tableElements = table.find_elements(By.XPATH, "//div/div[2]/div/div/div[3]")
    tableNames = []
    for element in tableElements:
        if(element.text != " "):
            tableNames.append(element.text)
    if(len(tableNames) == 0):
        print("[!] Names not found")
    else:
        print("[+] Names found successful")
    
    return tableNames

# Search answers from excel by name
def answersForName(nameList):
    for name in nameList:
        nameParsed = excel.parseData(name)
        print("-" + nameParsed + "-")
        print(excel.find_data(nameParsed))

if __name__ == '__main__':
    login(driver)
    goToTable(driver)
    names = getNamesFromTable(driver)
    answersForName(names)
