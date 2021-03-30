# -*- coding: utf-8 -*-
# @Author : bhl
# @File : contact_page.py
from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        pass

    def add_department(self):
        pass

    def get_list(self):
        '''
        返回通讯录页面信息
        :return:
        '''
        name_eles = self.find(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        name_list = []
        for ele in name_eles:
            name_list.append(ele.text)
        return name_list