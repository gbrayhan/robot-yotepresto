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
emailYTP = env("YTP_EMAIL")
for character in emailYTP:
    emailArea.send_keys(character)
    time.sleep(0.1)
emailArea.click()

continueButton = browser.find_elements_by_xpath("//input[@name='commit' and @value='Continuar']")[0]
continueButton.click()

time.sleep(1)

# click email password
password = browser.find_element_by_id('sessions_password')
time.sleep(0.1)
password.click()
time.sleep(0.1)

# enter pass
passYTP = env("YTP_PASS")
for character in passYTP:
    password.send_keys(character)
    time.sleep(0.1)
time.sleep(0.1)
password.click()

# click pass
iniciarButton = browser.find_elements_by_xpath("//input[@name='commit' and @value='Iniciar Sesión']")[0]
iniciarButton.click()

# Get values
time.sleep(3)
quantity = browser.find_elements_by_xpath("//div[@class='quantity' and @data-testid='fundingQuantity']")[0].text

print("El numero de solicitudes activas es: " + quantity)
