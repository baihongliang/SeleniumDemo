# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_form.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        ele = self.driver.find_element(By.ID,'login')
        ele.send_keys('123')
        print(ele.get_attribute("value"))
        self.driver.find_element(By.ID,'user_password').send_keys('123')
        self.driver.find_element(By.ID,'user_remember_me').click()
        self.driver.find_element(By.XPATH,'//*[@id="new_user"]/div[4]/input')
        sleep(2)