from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time



options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.amazon.in/")
list = driver.find_elements(By.XPATH, "(//div[@class='a-section a-spacing-none feed-carousel'])[2]//li[@class='feed-carousel-card']/span")

print(len(list))

for l in list:
    time.sleep(2)
    l.click()
    driver.back()

    
