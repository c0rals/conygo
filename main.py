from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dataExtraction import *
from time import sleep

# Driver setting
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait_short = WebDriverWait(driver,20)
wait_long = WebDriverWait(driver, 200)

# Login
def login(driver):
    driver.get("https://clinico.rayenaps.cl/")
    Ubicacion_input = driver.find_element(
        By.ID, "location")
    Usuario_input = driver.find_element(
        By.ID, "username")
    Clave_input = driver.find_element(
        By.ID, "password")

    Ubicacion_input.clear()
    Usuario_input.clear()
    Clave_input.clear()

    Usuario_input.send_keys("18621997k")
    Ubicacion_input.send_keys("csfclotarioblest")
    Clave_input.send_keys("1312LKcco")
    driver.find_element(By.CLASS_NAME, "btn-secondary").click()

    wait_short.until(EC.url_contains("main"))

    try:
        wait_short.until(EC.presence_of_element_located((By.CLASS_NAME, "cache-loading")))
        wait_long.until_not(EC.presence_of_element_located((By.CLASS_NAME, "cache-loading")))

        print("[+] Login success")
    except:
        print("[!] Login fail")
        pass
    return driver

# Navegate to list
def goToTable(driver):
    driver.find_element(
        By.ID, "navbar-main-menu").click()
    driver.find_element(
        By.XPATH, "//*[contains(text(), 'Box')]").click()
    driver.find_element(
        By.XPATH, "//*[contains(text(), 'Pacientes citados')]").click()
    try:
        wait_short.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.ReactTable.table-height")))
        wait_short.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.rt-thead.-header")))
        print("[+] Table load success")
    except:
        print("[!] Table load fail")
        pass
    return driver

# Get list of names (need to be valid names, not all names)
def getNamesFromTable(driver):
    try:
        wait_short.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div.rt-tr-group")))
    except:
        print("[!] Names not found")
        return

    tableElements = driver.find_elements(By.XPATH, "//*[@class='rt-table']/div[2]/div/div/div[3]")
    tableNames = []
    for element in tableElements:
        if(element.text != " "):
            tableNames.append(element.text)
    if(len(tableNames) == 0):
        print("[!] Names not found")
        return
    else:
        print("[+] Names found successful")

    return tableNames

# Click on website calendar by day
def click_calendar(driver,day):
    try:
        wait_short.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[1]/div[3]/div[1]/div/span[2]")))
    except:
        print("[!] Title bar not found")
        return

    try:
        wait_short.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[1]/div[3]/div[1]/div/span[2]/div/div")))
        driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[3]/div[1]/div/span[2]/div/div").click()
        print("[+] Calendar clicked")
        try:
            wait_short.until(EC.element_to_be_clickable((By.CLASS_NAME,"react-datepicker__month")))
            driver.find_element(By.XPATH,"//div[@class='react-datepicker__week']/div[contains(text(),'"+day+"')]").click()
            print("[+] Day "+day+" clicked")
        except:
            print("[!] Day not clicked")
    except:
        print("[!] Calendar not found")
        return


def clickName(driver,name):
    try:
        wait_short.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div.rt-tr-group")))
    except:
        print("[!] Names not found")
        return

    tableElements = driver.find_elements(By.XPATH, "//*[@class='rt-table']/div[2]/div/div/div[3]")

    for element in tableElements:
        if(name in element.text):
            element.click()
            print("[+] "+name+" clicked")
            return
    print("[!] "+name+" not found")
    return


if __name__ == '__main__':
    login(driver)
    goToTable(driver)
    click_calendar(driver,"28")
    names = getNamesFromTable(driver)
    answersForName(names)
    sleep(0.5)
    driver.close()