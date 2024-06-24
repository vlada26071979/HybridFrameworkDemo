import time

import pytest
from selenium import webdriver
from HybridFrameworkDemo.pageObjects.LoginPage import LoginPage

class TestLogin:
    base_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        expected_title = "Your store. Login"
        actual_title = self.driver.title
        self.driver.close()

        if actual_title == expected_title:
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        login_page = LoginPage(self.driver)
        login_page.enter_username(username=self.username)
        time.sleep(3)

        login_page.enter_password(password=self.password)
        time.sleep(3)

        login_page.click_login_button()
        time.sleep(3)

        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"
        self.driver.close()

        assert actual_title == expected_title, f"{actual_title} is not equal to {expected_title}"








