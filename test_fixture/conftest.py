import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(options=options)
    return driver
    # request.cls.driver = driver

    # yield

    # print("GOOD BYE")

    
