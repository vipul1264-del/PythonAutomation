from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import pytest
import time

options = Options()
options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options)


def test_one():
    driver = webdriver.Chrome(options=options)
    driver.get("https://in.skillup.online/")
    time.sleep(2)
    driver.maximize_window()
    driver.quit()



def test_two():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.pdfdrive.com/")
    time.sleep(2)
    driver.maximize_window()
    driver.quit()



def test_three():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.naukri.com/")
    time.sleep(2)
    driver.maximize_window()
    driver.quit()



