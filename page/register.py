# -*- coding: utf-8 -*-
# @Author : bhl
# @File : register.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,'corp_name').send_keys('hello')
        self.find(By.ID,'manager_name').send_keys('hello2')
        return True
