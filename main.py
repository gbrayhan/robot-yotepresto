import os
import time

from selenium import webdriver
from environs import Env

env = Env()
env.read_env()

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PATH_CHROMEDRIVER = env("PATH_CHROMEDRIVER")
DRIVER_BIN = os.path.join(PROJECT_ROOT, PATH_CHROMEDRIVER)

browser = webdriver.Chrome(executable_path=DRIVER_BIN)
urlLogin = env("URL_YTP_LOGIN")
browser.get(urlLogin)

# click email input
emailArea = browser.find_element_by_id('email-field-clone')
emailArea.click()

# enter email
emailYTP = env("YTP_EMAIL")
for character in emailYTP:
    emailArea.send_keys(character)
    time.sleep(0.15)
emailArea.click()

continueButton = browser.find_elements_by_xpath("//input[@name='commit' and @value='Continuar']")[0]
continueButton.click()

time.sleep(1)

# click email password
password = browser.find_element_by_id('sessions_password')
time.sleep(0.15)
password.click()
time.sleep(0.15)

# enter pass
passYTP = env("YTP_PASS")
for character in passYTP:
    password.send_keys(character)
    time.sleep(0.15)
time.sleep(0.15)
password.click()

# click pass
iniciarButton = browser.find_elements_by_xpath("//input[@name='commit' and @value='Iniciar Sesión']")[0]
iniciarButton.click()

# Get values
time.sleep(3)
quantity = browser.find_element_by_xpath("//div[@class='quantity']").text

acceptedQualification = ["A1", "A2", "A3", "A4", "A5", "A6", "A7",
                         "B1", "B2", "B3", "B4", "B5", "B6", "B7", "C1"]

if int(quantity) > 0:
    solicitudesExistentes = browser.find_element_by_xpath(
        "//*[contains(text(), 'Ir a prestar')]").find_element_by_xpath("..")
    solicitudesExistentes.click()
    time.sleep(2)
    qualification = browser.find_elements_by_xpath("//span[@class='qualification']")[0].text
    if qualification in acceptedQualification:
        print("Send EMAIL")
else:
    time.sleep(3)
    browser.close()

print("El numero de solicitudes activas es: " + quantity)
time.sleep(15)
browser.close()

