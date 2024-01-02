from DataDriven.Zenportal.webelements_locators.Selectors import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# in this class we creating methods for each functional elements and passing locators
class Login_details(Locators):

    def __init__(self, driver):
        self.driver = driver

    # username with locator
    def enter_value_login_id(self, name):
        self.driver.find_element(by=By.NAME, value=self.email_text).send_keys(name)

    # password with locator
    def enter_password(self, password):
        self.driver.find_element(by=By.NAME, value=self.password_text).send_keys(password)

    # Login_button with locator
    def click_login(self):
        self.driver.find_element(by=By.XPATH, value=self.login_button).click()

    # Logout_button with locator
    def click_logout(self):
        self.driver.find_element(by=By.XPATH, value=self.profile_img).click()
        logout_butt = self.driver.find_element(by=By.XPATH, value=self.logout_dropdown_button)
        action = ActionChains(self.driver)
        action.move_to_element(logout_butt).click().perform()


