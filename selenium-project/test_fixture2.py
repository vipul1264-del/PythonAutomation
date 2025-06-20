import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def test_demo():
    print("I am using the pytest fixtures")


def test_demo1():
    
    driver.get("https://www.facebook.com/")

def test_demo2():
    print("I am using the pytest fixtures")


def test_demo3():
    
    driver.get("https://www.instagram.com/")