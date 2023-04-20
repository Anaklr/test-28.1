from .base_page import BasePage
from .locators import AuthLocators
from .locators import RegisterLocators

import os

class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or " https://b2c.passport.rt.ru"
        driver.get(url)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.btn_forgot_password = driver.find_element(*AuthLocators.AUTH_BTN_FORGOT_PASSWORD)
        self.btn_personal_account = driver.find_element(*AuthLocators.AUTH_BTN_PERSONAL_ACCOUNT)
        self.btn_login = driver.find_element(*AuthLocators.AUTH_BTN_LOGIN)
        self.btn_mail = driver.find_element(*AuthLocators.AUTH_BTN_MAIL)
        self.btn_phone = driver.find_element(*AuthLocators.AUTH_BTN_PHONE)
        self.btn_register = driver.find_element(*AuthLocators.AUTH_BTN_REGISTER)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def btn_forgot_password_click(self):
        self.btn_forgot_password.click()

    def btn_personal_account_click(self):
        self.btn_personal_account.click()

    def btn_login_click(self):
        self.btn_login.click()

    def btn_mail_click(self):
        self.btn_mail.click()

    def btn_phone_click(self):
        self.btn_phone.click()

    def btn_register_click(self):
        self.btn_register.click()

class RegisterPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.first_name = driver.find_element(*RegisterLocators.REGISTER_FIRSTNAME)
        self.last_name = driver.find_element(*RegisterLocators.REGISTER_LASTNAME)
        self.email = driver.find_element(*RegisterLocators.REGISTER_ADDRESS)
        self.password = driver.find_element(*RegisterLocators.REGISTER_PASSWORD)
        self.password_confirm = driver.find_element(*RegisterLocators.REGISTER_PASSWORD_CONFIRM)
        self.btn = driver.find_element(*RegisterLocators.REGISTER_BTN)

    def enter_firstname(self, value):
        self.first_name.send_keys(value)

    def enter_lastname(self, value):
        self.last_name.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_pass_conf(self, value):
        self.password_confirm.send_keys(value)

    def btn_click(self):
        self.btn.click()