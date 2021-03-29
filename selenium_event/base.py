# -*- coding: utf-8 -*-
# @Author : bhl
# @File : base.py
from selenium import webdriver
import os


class Base:
    def setup(self):
        # Mac上，命令行运行 browser=chrome pytest test_*.py
        browser = os.getenv("browser")
        # print(browser)
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

