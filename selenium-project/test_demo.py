from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()


def test_demo():

    driver.get("https://www.amazon.in/")
    driver.find_element(By.XPATH,"//a[@class='a-link-normal']/img[contains(@alt,'Amazon Brand – Solimo Super Slide with Basketball for Indoor & Outdoor Use')]").click()
    driver.back()
    driver.execute_script("window.scrollTo(0, 1700)")