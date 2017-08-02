import os
from time import sleep
from appium import webdriver

def before_feature(context, feature):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = 'FA6AE0307800'
    desired_caps['appPackage'] = os.getenv('PGPKG')
    desired_caps['appActivity'] = os.getenv('PGPKG') + '.MainPage'
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def after_feature(context, feature):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_final.png")
    context.driver.quit()