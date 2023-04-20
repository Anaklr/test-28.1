from selenium.webdriver.common.by import By

class AuthLocators:
    "Локаторы страницы авторизации"
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    AUTH_BTN_FORGOT_PASSWORD = (By.ID, "forgot_password")
    AUTH_BTN_PERSONAL_ACCOUNT = (By.ID, "t-btn-tab-ls")
    AUTH_BTN_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_BTN_MAIL = (By.ID, "t-btn-tab-mail")
    AUTH_BTN_PHONE = (By.ID, "t-btn-tab-phone")
    AUTH_BTN_REGISTER = (By.ID, "kc-register")

class RegisterLocators:
    "Локаторы страницы регистрации"
    REGISTER_FIRSTNAME = (By.XPATH, "//input[@name='firstName']")
    REGISTER_LASTNAME = (By.XPATH, "//input[@name='lastName']")
    REG_REGION = (By.CLASS_NAME, "rt-input-container rt-select__input")
    REGISTER_ADDRESS = (By.ID, 'address')
    REGISTER_PASSWORD = (By.ID, 'password')
    REGISTER_PASSWORD_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    REGISTER_BTN = (By.XPATH, "//button[@name='register']")
