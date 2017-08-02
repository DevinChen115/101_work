# coding:utf-8
from behave import *
from time import sleep
# from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from nose.tools import assert_true
import os

@given(u'PG 開啟')
def step_impl(context):
  print("a")

@when(u'點擊 ＋ 號')
def step_impl(context,timeout = 3):
  WebDriverWait(context.driver, timeout).until(EC.element_to_be_clickable((By.ID, 'com.roidapp.photogrid:id/btn_fast_tools'))).click()

@then(u'我應該可以看到工具列')
def step_impl(context, timeout = 3):
  assert_true(WebDriverWait(context.driver, timeout).until(EC.visibility_of_element_located((By.ID, 'com.roidapp.photogrid:id/recent_data'))))

@when(u'click "{btn}"')
def step_impl(context,btn,timeout = 3):
    if (btn == "apps"):
    	WebDriverWait(context.driver, timeout).until(EC.element_to_be_clickable((By.ID, 'com.roidapp.photogrid:id/btn_fast_tools'))).click()


if __name__ == '__main__':
  context.driver = webdriver.Remote()
