# -*- coding: utf-8 -*-
# @Author : bhl
# @File : base_page.py
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, base_driver:WebDriver=None):
        # base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._set_cookie()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def find(self,by,locator):
        return self.driver.find_element(by, locator)

    def _get_cookie(self):
        # 复用浏览器或者暂停扫码登陆后，获取已登录的企业微信cookie并保存
        cookie = self.driver.get_cookies()
        # cookie = driver.get_cookies()
        with open("../testcase/cookie.json", 'w') as f:
        # with open("cookie.json", 'w') as f:
            json.dump(cookie, f)

    def _set_cookie(self):
        # 读取cookie
        with open("../testcase/cookie.json", "r") as f:
            cookies = json.load(f)
        # print(cookies)
        # 准备需要添加cookie的页面
        self.driver.get("https://work.weixin.qq.com/")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 打开企业微信登录后的"首页"页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 点击 客户联系
        # self.driver.find_element(By.CSS_SELECTOR, "#menu_customer").click()
        sleep(3)

    # def __del__(self):
    #     self.driver.quit()