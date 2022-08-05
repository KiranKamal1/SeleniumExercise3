from selenium.webdriver.common.by import By
from Locators.locators import websiteLocator
from Locators.locators import websiteLocatorType
from Locators.locators import otherelements

class homepage(object):

    def __init__(self,driver):
        self.driver=driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            return False


    def searchText(self,text):
        bytype  = self.getByType(websiteLocatorType.searchBoxType)
        searchText=self.driver.find_element(bytype,websiteLocator.searchBoxLocator)
        searchText.send_keys(text)

    def categories(self):
        bytype = self.getByType(websiteLocatorType.categoriesType)
        self.driver.find_element(bytype,websiteLocator.categoriesLocator).click()
        bytype = self.getByType(websiteLocatorType.categoriesDropdownType)
        self.driver.find_element(bytype, websiteLocator.categoriesDropdownLocator).click()

    def searchbtn(self):
        bytype = self.getByType(websiteLocatorType.searchbtnType)
        self.driver.find_element(bytype, websiteLocator.searchbtnLocator).click()

    def creatingFile(self,test_list,filename):
        file1 = open(filename,"w")
        for i in test_list:
            file1.write(str(i)+"\n")
        file1.close()


    def result1(self):
        bytype = self.getByType(websiteLocatorType.result1Type)
        oneElement = self.driver.find_element(bytype, websiteLocator.result1Locator)
        Elements2 = oneElement.find_elements(By.TAG_NAME,otherelements.tagname1)
        self.save_in_list(Elements2,"file1.txt")


    def save_in_list(self,Elements2,filename):
        a = 0
        test_list = []
        for element in Elements2:
            test_list.insert(a, element.text)
            a += 1

        self.creatingFile(test_list,filename)


    def pageProduct(self):
        Elements2=self.element_search()
        self.save_in_list(Elements2,"file2.txt")

    def nth_value(self,value):
        Elements2=self.element_search()
        a = 0
        test_list = []
        for element in Elements2:
            test_list.insert(a, element.text)
            a += 1
        value = value - 1
        for i in range(len(test_list)):
            if i == value:
                print(test_list[i])
                break

    def element_search(self):
        bytype = self.getByType(websiteLocatorType.productpageType)
        oneElement = self.driver.find_element(bytype, websiteLocator.productpagelocator)
        Elements2 = oneElement.find_elements(By.TAG_NAME, otherelements.tagname2)
        return Elements2


    def search_by_scroll(self):
        bytype = self.getByType(websiteLocatorType.scrollElementType)
        scrollElement = self.driver.find_element(bytype, websiteLocator.scrollElementLocator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scrollElement)

        Elements2=self.element_search()
        self.save_in_list(Elements2, "file3.txt")




