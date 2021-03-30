# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_add_member.py
from test_po.page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        # 实例化
        self.main = MainPage()

    def test_add_member(self):
        # 1.首页跳转到添加成员页 2.添加成员 3.获取成员信息
        result = self.main.goto_add_member().add_member().get_list()
        assert "cuisitana1" in result

    def test_add_member_fail(self):
        # 1.首页跳转到添加成员页 2.添加成员 3.获取成员信息
        result = self.main.goto_add_member().add_member_fail().get_list()
        assert "cuisitana1" not in result
