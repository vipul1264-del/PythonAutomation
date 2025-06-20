from test_conftest import Invoke_browser

class test_one(Invoke_browser):

    def __init__(self, driver):
        self.driver = driver

    def test_01(self):
        self.driver.get("https://www.youtube.com/")
