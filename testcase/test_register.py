# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_register.py
from page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()