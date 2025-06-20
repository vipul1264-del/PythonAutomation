from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

options = Options()  
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")


def test_action():
   
   driver.get("https://www.flipkart.com/")
  
   search_box = driver.find_element(By.XPATH,"//input[@type='text']")
   WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//Button[Text()='X']")))
   #time.sleep(4)
   login_popup_close_button = driver.find_element(By.XPATH, "//Button[Text()='X']")
   login_popup_close_button.click()
   action = ActionChains(driver, duration=2000)
   action.move_to_element(driver.find_element(By.XPATH,"((//div[@class='_2msBFL']//div)[20]//div)[2]//img")).click()