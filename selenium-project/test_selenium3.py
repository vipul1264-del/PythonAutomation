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


def test_one():
    check_boxes = driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
    print(len(check_boxes))
    for i in check_boxes:
        i.click()

@pytest.mark.sanity
def test_two():
    static_dropdown = driver.find_element(By.ID,"dropdown-class-example")
    select = Select(static_dropdown)
    select.select_by_index(1)
    time.sleep(2)
    select.select_by_value("option2")
    time.sleep(2)
    select.select_by_visible_text("Option3")
