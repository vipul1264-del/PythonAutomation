from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

@pytest.mark.smoke
def test_multiplewindow():
    
    driver.find_element(By.XPATH,"(//div[contains(@class,'block large-row-spacer')])[2]//button").click()
    time.sleep(5)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    # driver.find_element(By.XPATH,"(//div[contains(@class,'spacer')])[2]//a").click()

    print("#############################")
    blog = driver.find_element(By.XPATH,"//div[@id]//a[contains(@href,'/blog')]")
    blog.click()




    