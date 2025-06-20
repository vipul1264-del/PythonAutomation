from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)

def test_javascript():

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://in.skillup.online/")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, -200)")


    driver.save_screenshot("image.png")