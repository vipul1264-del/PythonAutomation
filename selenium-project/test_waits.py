from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


options = Options()
options.add_experimental_option("detach", True)

@pytest.mark.sanity
def test_wait():

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(2)
    driver.find_element(By.ID,'checkBoxOption1').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID,'checkBoxOption1').click()

    # Explicitwait
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID,'autocomplete')).click()


