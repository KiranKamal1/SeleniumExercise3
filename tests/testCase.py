from pages.websiteHomePage import homepage
from Configuration.configuration import SeleniumDriver


class test_ebaysearch(SeleniumDriver):

    def test_ebaysearch(self):
        es=homepage(self.driver)
        tc1=es.searchText("Apple Watch")
        tc2=es.categories()
        tc3=es.searchbtn()

        #search Result
        tc4=es.result1()

        #Display product on Page
        tc5=es.pageProduct()

        #Display nth Value
        tc6=es.nth_value(2)

        #Display products by scroll
        tc7=es.search_by_scroll()

        self.driver.quit()


