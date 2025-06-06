import time
import utils

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def start_scrapping(data: dict[str, str], duration: int) -> None:
    URL = data["url"]

    driver = webdriver.Firefox()
    driver.get(URL)

    result_file = open(data["result_path"], "w")

    wait = WebDriverWait(driver, 15)  # Espera até 10 segundos
    result_file.write("latency,objcache_value,valvache_value,memcached_value\n")

    try:
        end_time = time.time() + duration
        while time.time() < end_time:
            objcache_value = get_objcache_value(wait)
            valcache_value = get_valcache_value(wait)
            memcached_value = get_memcached_value(wait)
            avg_latency = get_average_latency(wait)

            result_file.write(
                f"{avg_latency},{objcache_value},{valcache_value},{memcached_value}\n"
            )
            time.sleep(1)  # 500 ms
    except KeyboardInterrupt:
        driver.quit()
        result_file.close()


def get_average_latency(wait) -> str:
    div = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".svelte-dw75hy"))
    )

    return utils.filter_number_from_string(div.text)


def get_objcache_value(wait) -> str:
    target_labels = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-label"))
    )

    objcache_label = target_labels[6]
    objcache_value = objcache_label.find_element(By.TAG_NAME, "code")
    if objcache_value is not None:
        objcache_usage_percentage = (
            float(utils.filter_number_from_string(objcache_value.text)) / 100
        )
        return f"{objcache_usage_percentage:.4f}"
    return "0.00"


def get_valcache_value(wait) -> str:
    valcache_enable_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#check-valcache"))
    )
    valcache_value = None
    if valcache_enable_button.is_selected():
        target_labels = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-label"))
        )

        valcache_label = target_labels[7]
        valcache_value = valcache_label.find_element(By.TAG_NAME, "code")
    if valcache_value is not None:
        valcache_usage_percentage = (
            float(utils.filter_number_from_string(valcache_value.text)) / 100
        )
        return f"{valcache_usage_percentage:.4f}"
    return "0.00"


def get_memcached_value(wait) -> str:
    memcached_enable_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#check-memcached"))
    )

    memcached_value = None
    if memcached_enable_button.is_selected():
        target_labels = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-label"))
        )

        memcached_label = target_labels[8]
        memcached_value = memcached_label.find_element(By.TAG_NAME, "code")

    if memcached_value is not None:
        memcached_usage_percentage = (
            float(utils.filter_number_from_string(memcached_value.text)) / 100
        )
        return f"{memcached_usage_percentage:.4f}"
    return "0.00"
