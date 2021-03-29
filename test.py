# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test.py
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_selenium():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com")

class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        # self.driver.find_element_by_id()
        self.driver.find_element(By.XPATH,"//*[@id='sk']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, 'su')))
