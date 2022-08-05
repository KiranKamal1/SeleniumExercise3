import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ebaysearching():

    def test1(self):
        baseUrl = "https://www.ebay.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        searchText = driver.find_element(By.ID, "gh-ac")
        searchText.send_keys("Apple Watch")

        categories=driver.find_element(By.CSS_SELECTOR,"[name='_sacat']").click()
        categories1=driver.find_element(By.CSS_SELECTOR,"[value='15032']").click()

        searching=driver.find_element(By.CSS_SELECTOR,"[value = 'Search']").click()
        time.sleep(5)

        test_list=[]
        #result1
        oneElement = driver.find_element(By.XPATH, "//div[@id='srp-river-results']/ul/li[1]")
        Elements2 = oneElement.find_elements(By.TAG_NAME, "div")
        time.sleep(2)
        a=0
        for element in Elements2:
            #print(element.text)
            test_list.insert(a,element.text)
            a+=1
            #if element.text==" - apply Series filter" or" - apply Band Color filter" or " - apply Case Size filter":
             #   test_list.pop()
            #else:
            #    a=a+1
        oneElement = driver.find_element(By.XPATH, "//div[@id='srp-river-results']/ul")
        Elements2 = oneElement.find_elements(By.TAG_NAME, "h3")
        time.sleep(2)
        a = 0
        test_list2=[]
        textToSelect2="Apple Watch Series 5 44mm Space Gray Case (GPS + Cellular) NO LCD AS IS"
        for element in Elements2:
            test_list2.insert(a, element.text)
            a+=1
        print("*#"*2)
        for i in range(len(test_list2)):
            print(test_list2[i])


        value=1
        value=value-1
        print("*#"*5)
        for i in range(len(test_list2)):
            if i==value:
                print(test_list2[i])
                break

        scrollElement = driver.find_element(By.XPATH, "/html//footer[@id='glbfooter']")
        driver.execute_script("arguments[0].scrollIntoView(true);", scrollElement)

        oneElement = driver.find_element(By.XPATH, "//div[@id='srp-river-results']/ul")
        Elements2 = oneElement.find_elements(By.TAG_NAME, "h3")
        time.sleep(2)
        a = 0
        test_list2 = []
        for element in Elements2:
            test_list2.insert(a, element.text)
            a+=1
        print("*#" * 2)
        for i in range(len(test_list2)):
            print(test_list2[i])
            print(i)

        driver.quit()




#if __name__ == '__main__':
 #   unittest.main()

ff=ebaysearching()
ff.test1()