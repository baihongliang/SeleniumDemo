# -*- coding: utf-8 -*-
# @Author : bhl
# @File : base.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()