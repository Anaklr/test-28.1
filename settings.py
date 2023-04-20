import os
from dotenv import load_dotenv
load_dotenv()


valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
register_first_name = os.getenv('first_name')
register_last_name = os.getenv('last_name')
register_email = os.getenv('register_email')
register_phone = os.getenv('register_phone')
register_phone_2 = os.getenv('register_phone_2')
register_password = os.getenv('register_password')
register_pass_conf = os.getenv('register_pass_conf')

def generate_string_rus(num):
    return 'л' * num

def generate_string_en(num):
    return 'f' * num

def figure(num):
    return '2' * num

def english_chars():
    return 'sdfjksashdksgdafdhjgjhgsdhf'

def russian_chars():
    return 'порплыпвыешвга'

def chinese_chars():    # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
    return '|\\/!@#$%^&*('