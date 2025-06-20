from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytest




class Invoke_browser:
    
    @pytest.fixture(autouse=True)
    def setup():

        options = Options()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        # driver.get("https://www.amazon.in/")
        driver.maximize_window()
        
        yield
        print("testcase executed successfully")
        print("close browser")