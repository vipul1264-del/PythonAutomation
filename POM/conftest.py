from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def browser_setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)


