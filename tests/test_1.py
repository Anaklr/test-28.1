from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By
import pytest
from settings import *


# тест 1. проверка поля ввода телефона

@pytest.mark.positive
@pytest.mark.parametrize('number', [valid_email, valid_phone],
                         ids=['valid_email', 'valid_phone'])

def test_auth_page_number_enter_figure(selenium, number):
    page = AuthPage(selenium)

    page.btn_phone.click()
    page.enter_email(number)
    selenium.implicitly_wait(3)
    page.enter_pass(valid_password)
    page.btn_click()
    selenium.implicitly_wait(3)

    assert page.get_relative_link() == '/account_b2c/page', "login error"


# тест 2. проверка поля ввода телефона

@pytest.mark.negative
@pytest.mark.parametrize('number', ['', figure(8), valid_phone, figure(10), figure(11)],
                         ids=['empty', 'figure_8', 'valid_phgone', 'figure_10', 'figure_11'])

def test_auth_page_number_enter_figure(selenium, number):
    page = AuthPage(selenium)
    page.btn_phone.click()
    page.enter_email(number)
    selenium.implicitly_wait(8)
    page.enter_pass(valid_password)
    page.btn_click()
    selenium.implicitly_wait(3)

    if (0 < len(number) < 10 and number.isdigit()) or len(number) == 0:
        wrong_format_number = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
        assert (wrong_format_number.text == "Неверный формат телефона") or\
               (wrong_format_number.text == 'Введите номер телефона')
    elif len(number) >= 10 and number.isdigit():
        form_error = selenium.find_element(By.ID, 'form-error-message')
        assert form_error.text == 'Неверный логин или пароль'

# тест 3. проверка поля ввода почты
@pytest.mark.positive
@pytest.mark.parametrize('email', [valid_email, valid_phone],
                         ids=['valid_email', 'valid_phone'])
def test_auth_page_email_enter_positive(selenium, email):
    page = AuthPage(selenium)
    page.btn_mail_click()
    selenium.implicitly_wait(5)
    page.enter_email(email)
    selenium.implicitly_wait(5)
    page.enter_pass(valid_password)
    page.btn_click()
    if len(email) != 0:
        assert page.get_relative_link() == '/account_b2c/page', "login error"


# тест 4. проверка забыл пароль
@pytest.mark.positive
def test_auth_page_forgot_password(selenium):
   page = AuthPage(selenium)
   selenium.implicitly_wait(5)
   page.btn_forgot_password.click()
   assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials', "login error"


# тест 5. проверка поля ввода пароль
@pytest.mark.negative
@pytest.mark.parametrize('password', ['', generate_string_rus(8), generate_string_en(256), valid_password,
                                       figure(8), figure(100)],
                         ids=['empty', '8 chars rus', '256 chars en', 'valid', '8 figure', '100 figure'])
def test_auth_page_password_enter_negative(selenium, password):
    page = AuthPage(selenium)
    page.btn_mail_click()
    selenium.implicitly_wait(5)
    page.enter_email(valid_email)
    selenium.implicitly_wait(5)
    page.enter_pass(password)
    page.btn_click()

    if len(password) == 0:
        assert page.get_relative_link() != '/account_b2c/page', "login error"
    else:
        mistake_form = selenium.find_element(By.ID, 'form-error-message')
        mistake = selenium.find_element(By.XPATH, '// *[ @ id = "page-right"] / div / div / h1')
        assert mistake_form.text == "Неверный логин или пароль" or mistake_form.text == \
               'Неверно введен текст с картинки' or mistake.text == "Ошибка"
        selenium.save_screenshot('result.png')


# тест 6. проверка поля логин
@pytest.mark.positive
@pytest.mark.parametrize('login', [valid_email, valid_phone],
                         ids=['valid_email', 'valid_phone'])
def test_auth_page_email_enter_positive(selenium, login):
    page = AuthPage(selenium)
    page.btn_login_click()
    selenium.implicitly_wait(5)
    page.enter_email(login)
    selenium.implicitly_wait(5)
    page.enter_pass(valid_password)
    page.btn_click()

    if len(login) != 0:
        assert page.get_relative_link() == '/account_b2c/page', "login error"


# тест 6. проверка поля логин
@pytest.mark.negative
@pytest.mark.parametrize('login', [russian_chars(), english_chars(), special_chars(), chinese_chars(), figure(20)],
                         ids=['russian_chars', 'english_chars', 'special_chars', 'chinese_chars', '20 figure'])
def test_auth_page_login_enter_negative(selenium, login):
    page = AuthPage(selenium)
    page.btn_login_click()
    page.enter_email(login)
    selenium.implicitly_wait(5)
    page.enter_pass(valid_password)
    selenium.implicitly_wait(5)
    page.btn_click()
    mistake = selenium.find_element(By.ID, 'form-error-message')
    assert mistake.text == "Неверный логин или пароль" or mistake.text == 'Неверно введен текст с картинки'


# тест 7. авторизации клиента по номеру л/с

@pytest.mark.positive
def test_auth_page_personal_account_pozitiv(selenium):
   page = AuthPage(selenium)
   page.btn_personal_account_click()
   page.enter_email(valid_email)
   selenium.implicitly_wait(5)
   page.enter_pass(valid_password)
   selenium.implicitly_wait(5)
   page.btn_click()

   assert page.get_relative_link() == '/account_b2c/page', "login error"


# тест 8. авторизация клиента по номеру л/с

@pytest.mark.negative
@pytest.mark.parametrize('personal_account', ['', figure(8), figure(12), valid_phone],
                         ids=['empty', 'figure_8', 'figure_12', 'valid_number'])
def test_auth_page_personal_account_negativ(selenium, personal_account):
   page = AuthPage(selenium)
   page.btn_personal_account_click()
   page.enter_email(personal_account)
   selenium.implicitly_wait(5)
   page.enter_pass(valid_password)
   selenium.implicitly_wait(5)
   page.btn_click()
   mistake = selenium.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
   form_error = selenium.find_element(By.ID, 'form-error-message')
   assert mistake.text == "Проверьте, пожалуйста, номер лицевого счета" or form_error.text == 'Неверный логин или пароль'
   assert page.get_relative_link() != '/account_b2c/page', "login error"
