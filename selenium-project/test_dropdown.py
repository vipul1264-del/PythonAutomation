from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import pytest
from test_conftest import Invoke_browser 


options = Options()  
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

@pytest.mark.smoke
def test_dropdown():
   dropdown = driver.find_element(By.ID,"dropdown-class-example")
   select = Select(dropdown)
   select.select_by_index(1)
   time.sleep(2)
   select.select_by_value("option2")
   time.sleep(2)
   select.select_by_visible_text("Option3")
   driver.find_element(By.XPATH,"//input[@value='radio1']").click()

def test_dynamicDropdown(): # this method for the stateforword
   driver.get("https://www.flipkart.com/")
   time.sleep(4)
   search_box = driver.find_element(By.XPATH,"//input[@type='text']")
   search_box.send_keys("one plus headphone")
   time.sleep(4)
   first_option = driver.find_element(By.XPATH,"(//form[contains(@class,'header-form-search')]//a)[1]")
   print(f"link present in first option  ::{first_option.get_attribute('href')}")
   print(f"text of first option ::{first_option.text}")
   first_option.click()
   print(driver.current_url)

@pytest.mark.smoke
def test_dynamicSelect():
   driver.get("https://www.flipkart.com/")
   time.sleep(4)
   search_box = driver.find_element(By.XPATH,"//input[@type='text']")
   search_box.send_keys("one plus")
   time.sleep(4)
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
      
       
