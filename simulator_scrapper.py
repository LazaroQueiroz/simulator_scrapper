import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

URL = os.getenv("URL")
CLASSE = os.getenv("CLASS")

driver = webdriver.Firefox()
driver.get(URL)

wait = WebDriverWait(driver, 10)  # Espera até 10 segundos
print("latency")
try:
    while True:
        div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, CLASSE)))
        print(f"Valor da div: {div.text}")
        time.sleep()  # 500 ms
except KeyboardInterrupt:
    driver.quit()
