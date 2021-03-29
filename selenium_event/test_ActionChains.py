# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_ActionChains.py
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
        # pass

    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element(By.XPATH,"//input[@value='click me']")
        ele_double_click = self.driver.find_element(By.XPATH,"//input[@value='dbl click me']")
        ele_right_click = self.driver.find_element(By.XPATH,"//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.double_click(ele_double_click)
        action.context_click(ele_right_click)
        action.perform()

    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com")
        # ele = self.driver.find_element_by_link_text("设置")
        ele = self.driver.find_element(By.XPATH, "//span[text()='设置']")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[contains(@class,'guide-close')]").click()
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        # action.move_to_element_with_offset(ele,1,1)
        action.perform()

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        sleep(3)
        drag_element = self.driver.find_element(By.ID,"dragger")
        drop_element = self.driver.find_element(By.XPATH,"/html/body/div[2]")
        drop_element2 = self.driver.find_element(By.XPATH,"/html/body/div[3]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element)
        # action.perform()
        action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element2).release().perform()
        sleep(3)

    def test_send_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        sleep(3)
        ele = self.driver.find_element(By.XPATH, "/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()