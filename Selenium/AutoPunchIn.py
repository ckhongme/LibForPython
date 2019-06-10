from selenium import webdriver
from selenium.webdriver.common.keys import Keys


webUrl = "http://www.manew.com/member.php?mod=logging&action=login"
username = "ckhonglogin@163.com"

#www.jianshu.com/sign_in

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(webUrl)

element = browser.find_element_by_id('username_Lwkzl')
element.clear()
element.send_keys(username)

#element = browser.find_element_by_id('password3_Lwkzl')
#element.clear()
#lement.send_keys('123' + Keys.ENTER)

#button = browser.find_element_by_name('loginsubmit')
#button.click()



