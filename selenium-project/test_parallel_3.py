from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import pytest

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

def test_three():
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
