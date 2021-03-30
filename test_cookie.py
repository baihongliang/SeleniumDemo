# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_cookie.py
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:
    def setup(self):
        # chrome_arg = webdriver.ChromeOptions()
        # chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_getcookie(self):
        # 复用浏览器或者暂停扫码登陆后，获取已登录的企业微信cookie并保存
        cookie = self.driver.get_cookies()
        with open("cookie.json", 'w') as f:
            json.dump(cookie, f)

    def test_usecookie(self):
        # 读取cookie
        with open("cookie.json", "r") as f:
            cookies = json.load(f)
        # print(cookies)
        # 准备需要添加cookie的页面
        self.driver.get("https://work.weixin.qq.com/")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 打开企业微信登录后的"首页"页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 点击 客户联系
        self.driver.find_element(By.CSS_SELECTOR,"#menu_customer").click()
        sleep(3)


