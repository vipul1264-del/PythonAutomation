from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import pytest

options = Options()  
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

@pytest.mark.sanity
def test_one():    
    driver.find_element(By.ID,"checkBoxOption1").click()
    driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
    driver.back()
    driver.find_element(By.PARTIAL_LINK_TEXT,"ResumeAssistance").click()
    driver.back()

def test_two():
    driver.find_element(By.CLASS_NAME,"blinkingText").click()
    driver.back()
    driver.find_element(By.XPATH,'//input[@value="radio2"]').click()
    driver.find_element(By.XPATH,'//input[@value="radio3" and @name="radioButton"]').click()

def test_three():
    text = (driver.find_element(By.XPATH,"//legend[text()='Suggession Class Example']").text)
    print(text)

# @pytest.fixture("skip")


