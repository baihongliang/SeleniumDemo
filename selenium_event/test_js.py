# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_js.py
from time import sleep

from selenium.webdriver.common.by import By

from selenium_event.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        # self.driver.execute_script("return document.getElementById('su')").click()
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        sleep(1)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element(By.XPATH,'//*[@id="page"]/div/a[10]').click()
        sleep(3)
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script('return document.title;'))
        print(self.driver.execute_script('return JSON.stringify(performance.timing);'))

    def test_js_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        date_js = "document.getElementById('train_date').removeAttribute('readonly')"
        self.driver.execute_script(date_js)
        sleep(2)
        date_js_1 = "document.getElementById('train_date').value='2021-04-15'"
        self.driver.execute_script(date_js_1)
        sleep(2)
        print("打印")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        print(f'当前日期为：{self.driver.find_element(By.ID,"train_date").get_attribute("value")}....')
        sleep(3)
