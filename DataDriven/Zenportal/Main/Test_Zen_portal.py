import pytest
from DataDriven.Zenportal.pom.main import Zen_portal_method

class Test_Webpage_Zen:

    @pytest.mark.usefixtures("setup_teardown") # we can conftest.py in any by use_fixture method
    def test_login_functionality(self):
        source = Zen_portal_method(self.driver) # creating instance object for class
        # we passing excel file_name and sheet_name
        source.read_and_write_data_in_excel_file("report_zen_portal1.xlsx", "Sheet1")

