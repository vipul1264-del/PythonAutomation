from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Refrigerators").click()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"Home & Kitc").click()
driver.back()
time.sleep(2)
driver.find_element(By.XPATH, "//img[contains(@alt, 'boAt')]").click()
driver.back()
time.sleep(2)
print("elements")
elements = driver.find_elements(By.CLASS_NAME,"product-image")
print(len(elements))



    
    