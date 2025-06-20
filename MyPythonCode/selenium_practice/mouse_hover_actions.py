from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

actions = ActionChains(driver)

hover_element = driver.find_element(By.ID,'mousehover')

actions.move_to_element(hover_element).perform()
actions.click(hover_element).perform()

