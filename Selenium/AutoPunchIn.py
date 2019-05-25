from selenium import webdriver
from selenium.webdriver.common.keys import Keys


webUrl = "https://www.baidu.com"


#www.jianshu.com/sign_in

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(webUrl)
#browser.find("name", "username").send_keys("13612966440")

element = browser.find_element_by_id('kw')
element.send_keys("Python" + Keys.ENTER)



