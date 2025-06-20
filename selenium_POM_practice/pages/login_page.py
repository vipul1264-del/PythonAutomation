from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.XPATH,"(//input[contains(@class,'_55r1')])[1]")
        self.pass_textbox = (By.XPATH,"//input[contains(@class,'9npi')]")
        self.login_button = (By.XPATH,"//button[contains(@class,'4jy6')]")

    def open_url(self, url):
        self.driver.get(url)

    def enterEmail(self, email):
        pass