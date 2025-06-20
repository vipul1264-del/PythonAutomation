import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_experimental_option("detach", True)
 
def test1(setup):
    driver = setup
    # driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print("fixture executed")
    driver.close()

