# coding=utf-8
from appium import webdriver
caps={
    'platformName':'Android',
    'platformVersion':'10',
    'deviceName':'MKB4C20619029439',
    'appPackage':' com.shuixin.sns.test',
    'appActivity':'com.shuixin.sns.SplashActivity',
    'noReset':True,
    'unicodeKeyboard':True,
    'resetKeyboard':True}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
# driver.find_element_by_xpath()




