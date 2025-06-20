from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
title = driver.title
print(f"the page title is :: {title}")
current_URL = driver.current_url
print(f"current URL is  :: {current_URL}")
page_source = driver.page_source
# print(f"the page source is :: {page_source}")

driver.get("https://www.google.com/")
title = driver.title
print(f"the page title is :: {title}")
# time.sleep(5)
driver.back()
# time.sleep(5)
driver.forward()
