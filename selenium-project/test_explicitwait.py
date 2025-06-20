from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

options = Options()  
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

def test_dynamicSelect():
   driver.get("https://www.flipkart.com/")
  
   search_box = driver.find_element(By.XPATH,"//input[@type='text']")
   WebDriverWait(driver, 2, 0.2).until(EC.visibility_of_element_located((By.XPATH, "//Button[Text()='X']")))
   login_popup_close_button = driver.find_element(By.XPATH, "//Button[Text()='X']")
   login_popup_close_button.click()
   search_box.send_keys("one plus")
   WebDriverWait(driver, 5).until(EC.presence_of_element_located(("XPATH","(//form[contains(@class,'header-form-search')]//a)")))
   dropdown_option = driver.find_elements(By.XPATH,"(//form[contains(@class,'header-form-search')]//a)")
   for index, options in enumerate(dropdown_option): # enumerate is used for get the index 
       print(f"link present in {index+1} option  ::{options.get_attribute('href')}")
       print(f"text of {index+1} option ::{options.text}")
       if "headphone" in options.text:
          options.click()
          print(driver.current_url)
          break
   else:
       print("headphone options  not found")