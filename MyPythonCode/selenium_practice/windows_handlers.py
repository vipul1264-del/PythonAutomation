from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options  = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/windows") 

driver.find_element(By.LINK_TEXT, 'Click Here').click()
parent_text = driver.find_element(By.XPATH, "//div[contains(@class,'example')]/h3").text
print(parent_text)

child_windows = driver.window_handles # it will return the list of the chlid windows
for i in child_windows: # it will call each child windows one by one
    driver.switch_to.window(i) # it will click each child windows one by one

child_text = driver.find_element(By.XPATH, "//div[contains(@class,'example')]/h3").text
print(child_text)

parent_windows = driver.current_window_handle #it will again switch the parent window

parent_text = driver.find_element(By.XPATH, "//div[contains(@class,'example')]/h3").text
print(parent_text)


