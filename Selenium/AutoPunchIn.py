from selenium import webdriver
from selenium.webdriver.common.keys import Keys


webUrl = "https://www.baidu.com"


#www.jianshu.com/sign_in

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(webUrl)
#browser.find("name", "username").send_keys("13612966440")

elements = browser.find_elements_by_id('kw')
elements.clear()
time.sleep(2)
elements.send_keys(py + Keys.ENTER)



