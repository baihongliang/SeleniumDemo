# -*- coding: utf-8 -*-
# @Author : bhl
# @File : add_member.py
from time import sleep

from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID,"username")
    def add_member(self):
        # 输入成员信息，点击保存
        self.find(*self._username).send_keys("cuisitana1")
        self.find(By.ID,"memberAdd_acctid").send_keys("cuisitana1")
        self.find(By.ID,"memberAdd_phone").send_keys("18200000004")
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self):
        # *代表解元组
        self.find(*self._username).send_keys("cuisitana1")
        self.find(By.ID, "memberAdd_acctid").send_keys("cuisitana1")
        self.find(By.ID, "memberAdd_phone").send_keys("18200000004")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return ContactPage(self.driver)