# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_TouchAction.py
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from time import sleep


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element(By.ID, 'kw')
        ele_s = self.driver.find_element(By.ID, 'su')
        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_s)
        action.perform()
        action.scroll_from_element(ele, 0, 10000)
        action.perform()
        sleep(1)
