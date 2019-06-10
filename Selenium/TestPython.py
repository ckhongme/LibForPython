from selenium import webdriver
from selenium.webdriver.common.keys import Keys


webUrl = "https://www.baidu.com"
search = "Python"

#www.jianshu.com/sign_in

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(webUrl)

element = browser.find_element_by_id('kw')
element.clear()
element.send_keys(search)
#element.click()




