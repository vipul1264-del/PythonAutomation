from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options  = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/") 

driver.find_element(By.XPATH,"//input[contains(@id,'alertbtn')]").click()

driver.implicitly_wait(5)

driver.switch_to.alert.accept()

# driver.switch_to.alert.dismiss()




