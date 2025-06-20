# from utilities.baseClass import BaseClass
import pytest
from selenium_POM_practice.tests.conftest import Setup


# @pytest.mark.usefixtures("setup")
class TestOne(Setup):
    
    def test_one(self):
      
      self.driver.get("https://www.facebook.com/")
    
      