from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options  


@pytest.mark.regression
def test_one():

    options = Options()
    options.add_experimental_option("detach", True)
              
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
            






