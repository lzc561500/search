from base.common_function import Fuction
from base.base_xpath import Xpath

class Search(Fuction):
    loc1=("id","com.android.settings:id/search")
    loc2=("xpath","//*[contains(@text,'搜索…')]")
    loc3=("class name","android.widget.ImageButton")

    def searchPage(self,text):
        self.element_click(self.loc1)
        self.send_keys(self.loc2,text)
        self.element_click(self.loc3)
