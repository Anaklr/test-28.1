from pages.auth_page import AuthPage
from pages.auth_page import RegisterPage
from selenium.webdriver.common.by import By
import pytest
from settings import *


# тест 9. проверка работы кнопки зарегистрироваться
@pytest.mark.positive
def test_register_page(selenium):
   page = AuthPage(selenium)
   selenium.implicitly_wait(5)
   page.btn_register.click()
   register = selenium.find_element(By.XPATH, '//h1[@class="card-container__title"]')
   assert register.text == "Регистрация"
   # Переход на страницу регистрации
   assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"


# тест 10. проверка поля ввода имя
@pytest.mark.negative
@pytest.mark.parametrize('firstname', ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(), chinese_chars(),
                                       special_chars(), 11111],
                         ids=['empty', 'one char', '31 chars', '256 chars', 'english', 'chinese',
                              'special', 'number'])
def test_registration_invalid_firstname(selenium, firstname):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(selenium)
    page.btn_register.click()
    selenium.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"

    page = RegisterPage(selenium)
    # Вводим имя:
    page.enter_firstname(firstname)
    selenium.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(register_last_name)
    selenium.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(register_email)
    selenium.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(register_password)
    selenium.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(register_pass_conf)
    selenium.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_meta = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
    assert error_meta.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# тест 11. проверка поля ввода имя
@pytest.mark.positive
@pytest.mark.parametrize('firstname', ['-', generate_string_rus(2), generate_string_rus(30),
                                       generate_string_rus(15)],
                         ids=['-', '2 char', '30 chars', '15 chars'])
def test_registration_valid_firstname(selenium, firstname):
    """Негативные сценарии регистрации на сайте, невалидный формат имени"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(selenium)
    page.btn_register.click()
    selenium.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"

    page = RegisterPage(selenium)
    # Вводим имя:
    page.enter_firstname(firstname)
    selenium.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(register_last_name)
    selenium.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(register_email)
    selenium.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(register_password)
    selenium.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(register_pass_conf)
    selenium.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    confirmation_email = selenium.find_element(By.CLASS_NAME, 'card-container__title')
    assert confirmation_email.text == 'Подтверждение email'


#  тест 12. проверка поля ввода фамилия
@pytest.mark.negative
@pytest.mark.parametrize('lastname', ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(), chinese_chars(),
                                       special_chars(), 11111],
                         ids=['empty', 'one char', '31 chars', '256 chars', 'english', 'chinese',
                              'special', 'number'])
def test_registration_invalid_lastname(selenium, lastname):
    """Негативные сценарии регистрации на сайте, невалидный формат имени"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(selenium)
    page.btn_register.click()
    selenium.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"

    page = RegisterPage(selenium)
    # Вводим имя:
    page.enter_firstname(register_first_name)
    selenium.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(lastname)
    selenium.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(register_phone)
    selenium.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(register_password)
    selenium.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(register_pass_conf)
    selenium.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    error_meta = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
    assert error_meta.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


#  тест 13. проверка поля ввода почта
@pytest.mark.negative
@pytest.mark.parametrize('email', ['', '@', '@.', '.', f'{russian_chars()}@mail.ru',
                                   f'{chinese_chars()}@mail.ru', f'{special_chars()}@mail.ru', 11111],
                         ids=['empty', '@', '@ and point', 'point', 'russian format', 'chinese format',
                              'special format', 'number'])
def test_registration_invalid_email(selenium, email):
    """Негативные сценарии регистрации на сайте, невалидный формат имени"""
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(selenium)
    page.btn_register.click()
    selenium.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"

    page = RegisterPage(selenium)
    # Вводим имя:
    page.enter_firstname(register_first_name)
    selenium.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(register_last_name)
    selenium.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(email)
    selenium.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(register_password)
    selenium.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(register_pass_conf)
    selenium.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    error_meta = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
    assert error_meta.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


# тест 14. проверка поля ввода пароль
@pytest.mark.negative
@pytest.mark.parametrize('password', ['', generate_string_rus(7),
                                       generate_string_en(7), generate_string_rus(21),
                                       generate_string_en(21), figure(7), figure(21)],
                         ids=['empty', '7 chars rus', '7 chars en', '21 chars rus', '21 chars en', '7 figure',
                              '21 figure'])
def test_registration_invalid_len_password(selenium, password):
    """Негативные сценарии регистрации на сайте, невалидный формат имени"""
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(selenium)
    page.btn_register.click()
    selenium.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"

    page = RegisterPage(selenium)
    # Вводим имя:
    page.enter_firstname(register_first_name)
    selenium.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(register_last_name)
    selenium.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(register_email)
    selenium.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(password)
    selenium.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(password)
    selenium.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    for i in range(len(password)):
        error_meta = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
        if  len(password) >= 0 and len(password) <9:
            assert error_meta.text == 'Длина пароля должна быть не менее 8 символов'
        elif len(password) > 20:
            assert error_meta.text == 'Длина пароля должна быть не более 20 символов'


 # тест 15. проверка поля ввода пароль
@pytest.mark.positive
@pytest.mark.parametrize('password', ['Qwerty6566596', 'Qwertyfdfd%$', register_password],
                         ids=['upper_lower_finger', 'upper_lower_spec', 'register_password'])
def test_registration_valid_password(selenium, password):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(selenium)
    page.btn_register.click()
    selenium.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"

    page = RegisterPage(selenium)
    # Вводим имя:
    page.enter_firstname(register_first_name)
    selenium.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(register_last_name)
    selenium.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(register_email)
    selenium.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(password)
    selenium.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(password)
    selenium.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    for i in range(len(password)):
        confirmation_email = selenium.find_element(By.CLASS_NAME, 'card-container__title')
        if 0 < len(password) < 21:
            for i in password:
                if i.isupper() and i.islower() and (i.isdigit()) or (i is special_chars()) and (i is not russian_chars()):
                    assert (confirmation_email.text == 'Подтверждение email') or \
                           (confirmation_email.text == 'Подтверждение телефона')


#  тест 16. проверка поля ввода подтверждение пароля
@pytest.mark.negative
@pytest.mark.parametrize('pass_conf', ['PASSWORD26', 'Ekjhksdfsdfasf', 'fsdagdsaghgdch',
                                       '3546546543533', 'hgfhgfgfh25', russian_chars(), special_chars(), 'Qwerty256'],
                         ids=['upper_finger', 'upper_lower', 'lower', 'finger', 'lower_finger',
                              'rus_chars', 'spec_chars', 'valid_form'])
def test_registration_invalid_pass_conf(selenium, pass_conf):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(selenium)
    page.btn_register.click()
    selenium.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration', "login error"

    page = RegisterPage(selenium)
    # Вводим имя:
    page.enter_firstname(register_first_name)
    selenium.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(register_last_name)
    selenium.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(register_email)
    selenium.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(register_password)
    selenium.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(pass_conf)
    selenium.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    for i in range(len(pass_conf)):
        error_meta = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
        if 0 < len(pass_conf) < 21:
            for i in pass_conf:
                if (i is not i.isupper()) or (i is not i.islower()) or ((i is not i.isdigit()) or (i is not special_chars())) or\
                        (i is russian_chars()):
                    assert (error_meta.text == 'Пароль должен содержать хотя бы одну заглавную букву') or \
                           (error_meta.text == 'Пароль должен содержать хотя бы одну прописную букву') or \
                           (error_meta.text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру') or \
                           (error_meta.text == 'Пароль должен содержать только латинские буквы')
                elif i.isupper() and i.islower() and (i.isdigit()) or (i is special_chars()) and \
                        (i is not russian_chars()) and pass_conf != register_password:
                    assert error_meta.text == 'Пароли не совпадают'


