# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_up_file.py
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium_event.base import Base


class TestUpFile(Base):
    def test_up_file(self):
        self.driver.get("https://image.baidu.com")
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.CLASS_NAME,'st_camera_off').click()
        ele = self.driver.find_element(By.ID,'stfile')
        ele.send_keys("/Users/baihongliang/PycharmProjects/SeleniumDemo/selenium_event/images/test.png")
        sleep(10)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        ele1 = self.driver.find_element(By.ID, 'draggable')
        ele2 = self.driver.find_element(By.ID, 'droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1,ele2).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, 'submitBTN').click()
        sleep(2)
