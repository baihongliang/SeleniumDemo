# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_window.py
from selenium.webdriver.common.by import By
from time import sleep
from selenium_event.base import Base



class TestForm(Base):

    def test_window(self):
        self.driver.get("https:www.baidu.com")
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[contains(@class,'guide-close')]").click()
        self.driver.find_element(By.XPATH,"//div[@id='u1']/a").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        sleep(2)
        self.driver.find_element(By.XPATH,"//a[contains(text(),'立即注册')]").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        sleep(2)
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys("username")

        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(2)