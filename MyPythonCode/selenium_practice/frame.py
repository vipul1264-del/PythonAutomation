from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options  = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/iframe") 

driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()
driver.implicitly_wait(2)
driver.back
driver.implicitly_wait(2)
driver.switch_to.frame("mce_0_ifr")

frame_text = driver.find_element(By.XPATH, "//body[(@id='tinymce')]/p").text
print(frame_text)

driver.switch_to.parent_frame()
driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()