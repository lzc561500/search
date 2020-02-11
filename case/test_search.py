import time

from base.connect_mobile import TestConnetMobile
from page.search_page import Search
import pytest
from base.base_yml import Data_key


class TestSearch:
    data_key=Data_key()

    def setup_class(self):
        self.driver = TestConnetMobile().connectMobile()

    @pytest.mark.parametrize("content",data_key.data_yml_key("search.yml","test_search"))
    def test_search(self,content):
        Search(self.driver,10,1).searchPage(content)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()