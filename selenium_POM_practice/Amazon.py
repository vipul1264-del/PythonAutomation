from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(2)
action = ActionChains(driver)
element = driver.find_element(By.XPATH,"//a[@data-nav-role='signin']")
action.move_to_element(element)
element.click()

email = driver.find_element(By.XPATH,"//input[starts-with(@class,'a-input-text a-span12')]")
email.send_keys("vipul1264@gmail.com")
time.sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
driver.find_element(By.XPATH,"//span[@id='continue']").click()
password = driver.find_element(By.XPATH,"//input[contains(@class,' a-span12 auth-autofocus')]")
password.send_keys("vipul@1264")
# driver.find_element(By.XPATH,"(//div[@class='a-section'])[last()]//div//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()