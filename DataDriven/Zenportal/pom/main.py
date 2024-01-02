from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from DataDriven.Zenportal.Excel.read_and_write_excel import Excel_funtion
from DataDriven.Zenportal.methods.methods_element import Login_details
from DataDriven.Zenportal.webelement_values.Values import Value

# here we are using POM model to combine all methods and class to create script for zen_portal login functions
class Zen_portal_method(Excel_funtion, Value):

    def __init__(self, driver):
        self.driver = driver

    # here get expected_values from excel_file and write actual_results to excel_file
    def read_and_write_data_in_excel_file(self, file, sheet_name):
        row = self.row_count(file, sheet_name)
        date_time = datetime.now()
        for row in range(2, row-1):
            username = self.read_data(file, sheet_name, row,  6)
            password = self.read_data(file, sheet_name, row, 7)
            source = Login_details(self.driver) # instance for class
            source.enter_value_login_id(username) # calling from methods class
            source.enter_password(password)
            source.click_login()
            # test PASS or FAIL
            try:
                # in this valid creditional means it navigates to next page it write test pass in excel file and click logout button and  came to homepage
                WebDriverWait(self.driver, 5).until(ec.url_to_be(self.dashboard_url)) # wait for navigate class page
                print("SUCCESS : Login success with username {a}".format(a=username))
                self.write_data(file, sheet_name, row, 3, date_time)
                self.write_data(file, sheet_name, row, 8, "TEST PASS")
                source.click_logout()

            except:
                # wait if invalid creditional means test will be fail and again refresh continue in home page
                WebDriverWait(self.driver, 1).until(ec.url_to_be(self.base_url))
                print("FAIL : Login failure with username {a}".format(a=username))
                self.write_data(file, sheet_name, row, 3, date_time)
                self.write_data(file, sheet_name, row, 8, "TEST FAIL")
                self.driver.refresh()

