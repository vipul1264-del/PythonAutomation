from selenium.webdriver.chrome import webdriver
from base_Pages.login_Page import Login_Page
import pytest

class test_Login:
    page_url = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    username = "vipul1264@gmail.com"
    password = "vipul@1264"

    def test_login(self):
        self.driver = webdriver.chrome()
        self.driver.get(self.page_url)
        self.lp = Login_Page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.click_continue_button()
        self.lp.enter_password(self.password)
        self.lp.click_signin_button()
        
        