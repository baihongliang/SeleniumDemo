# -*- coding: utf-8 -*-
# @Author : bhl
# @File : main_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By


from test_po.page.add_member import AddMemberPage
from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        return ContactPage(self.driver)

    def goto_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_item_title").click()
        return AddMemberPage(self.driver)