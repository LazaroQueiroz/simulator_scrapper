import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json
from dotenv import load_dotenv, dotenv_values


def formatLatency(a: str) -> str:
    n_s = "".join(list(filter(lambda x: x.isdigit() or x == ".", div.text)))
    f = float(n_s)
    s = f"{f:.2f}"
    return s


load_dotenv()

URL = os.getenv("URL")
CLASSE = os.getenv("CLASS")

driver = webdriver.Firefox()
driver.get(URL)


data = {}
data_file = open("config.json", "r")
data = json.load(data_file)

result_file = open(data["result_path"], "w")

wait = WebDriverWait(driver, 15)  # Espera até 10 segundos
result_file.write("latency\n")

try:
    while True:
        div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, CLASSE)))
        result_file.write(f"{formatLatency(div.text)}\n")
        time.sleep(1)  # 500 ms
except KeyboardInterrupt:
    driver.quit()
    result_file.close()
    data_file.close()
