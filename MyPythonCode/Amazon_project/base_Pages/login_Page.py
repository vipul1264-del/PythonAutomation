from selenium_Dec import webdriver
from selenium.webdriver.common.by import By
import pytest

class Login_Page:
    textbox_useremail_id = "ap_email"
    button_continue_id = "continue"
    textbox_password_id = "ap_password"
    button_signin_id = "signInSubmit"

    def __init(self, driver):
        self.driver = driver
    
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_useremail_id).clear()
        self.driver.find_element(By.ID, self.textbox_useremail_id).sendkeys(username)

    def click_continue_button(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.fing_element(By.ID, self.textbox_password_id).sendKeys(password)

    def click_signin_button(self):
        self.driver.find_element(By.ID, self.button_signin_id).click()