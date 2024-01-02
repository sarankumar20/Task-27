from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from DataDriven.Zenportal.webelement_values.Values import Value
import pytest


@pytest.fixture
def setup_teardown(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(Value.base_url)
    driver.implicitly_wait(20)
    request.cls.driver=driver
    yield
    driver.quit()

