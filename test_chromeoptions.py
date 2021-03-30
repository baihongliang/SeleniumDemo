# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_chromeoptions.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestChromeOptions:
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        # self.driver.find_element_by_id()
        self.driver.get("https://work.weixin.qq.com/")
        sleep(2)
        # 点击 企业登录
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        sleep(2)
        # 复用浏览器（已登录），点击通讯录
        self.driver.find_element(By.CSS_SELECTOR,"#menu_contacts").click()
        # 点击 客户联系
        self.driver.find_element(By.CSS_SELECTOR,"#menu_customer").click()
        sleep(3)