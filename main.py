from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="")  # if string stays empty (driver not specified) it will search for the driver by itself
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")


product_price_prefix = "productPrice"

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"promptContentChangeLanguage"))
)

language_selector = driver.find_element(By.ID, "langSelect-EN")
language_selector.click()

WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.ID, "bigCookie"))
 )
time.sleep(2)
bigCookie = driver.find_element(By.ID, "bigCookie")
for click in range(2000):
    time.sleep(0.1)
    bigCookie.click()
    cookieCount = driver.find_element(By.ID,"cookies").text.split(" ")[0]
    cookieCount = int(cookieCount.replace(",",""))

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookieCount >= product_price:
            time.sleep(0.3)
            upgrade = driver.find_element(By.XPATH, f"//div[@id='product{str(i)}']")
            upgrade.click()
            break


time.sleep(18)
driver.quit()
