# -*- coding: utf-8 -*-
# @Author : bhl
# @File : test_frame.py
import pytest
from selenium.webdriver.common.by import By
from selenium_event.base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element(By.ID, 'draggable').text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)


if __name__ == "__main__":
    pytest.main(['s', 'v', 'test_frame.py'])
