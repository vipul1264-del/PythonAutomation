from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
select = Select(driver.find_element(By.XPATH,"//select[contains(@id,'dropdown-class-example')]"))
select.select_by_visible_text("Option2")
time.sleep(3)
select.select_by_value("option3")
time.sleep(3)
select.deselect_by_index(0)

check_boxes = driver.find_elements(By.XPATH,"//input[contains(@type,'checkbox')]")
print(len(check_boxes))

for i in check_boxes:
    i.click()
