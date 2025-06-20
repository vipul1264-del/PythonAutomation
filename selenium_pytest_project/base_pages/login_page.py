from selenium.webdriver.common.by import By
from selenium import webdriver

class Login_page:
    textbox_email_id = "ap_email"
    btn_continue_id = "continue"
    textbox_password_id = "ap_password"
    btn_signin_xpath = "//input[@type='submit']"

# by using the self.driver we can use the class variables
    def __init__(self, driver):
        self.driver = driver

# write action methods

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(username)

    def click_continue_btn(self):
        self.driver.find_element(By.ID, self.btn_continue_id).click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_signin_xpath).click()