import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

def test_brokenlink():
    driver.get("https://jqueryui.com/")
    driver.maximize_window()
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(f"The total number of links are present on the pages are :: {len(all_links)}")

    for link in all_links:
        href = link.get_attribute('href')
        response = requests.get(href)

        if response.status_code >= 400:            
            print(f"Broken links: {href}  (status code: {response.status_code}")
            driver.quit()
            
        
