import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

class Insta(object):
    def insta_login(self):
        login_url = 'https://www.instagram.com/accounts/login/'
        user_id = 'ahnju96@gmail.com'
        user_pw = 'alTmfk8316'
        login_option = 'instagram'
        driver_path = 'chromedriver_win32/chromedriver.exe'
        driver = wd.Chrome(driver_path)
        insta_id = 'username'
        insta_pw = 'password'
        insta_login_btn = '.sqdOP.L3NKy.y3zKF     '
        print(f'login start - option : {login_option}')
        driver.get(login_url)
        time.sleep(5)
        try:
            insta_id_form = driver.find_element_by_name(insta_id)
            insta_id_form.send_keys(user_id)
            time.sleep(5)
            insta_pw_form = driver.find_element_by_name(insta_pw)
            insta_pw_form.send_keys(user_pw)
            time.sleep(5)
            login_ok_button = driver.find_element_by_css_selector(insta_login_btn)
            login_ok_button.click()
            is_login_success = True
        except:
            print('login FAIL')
            is_login_success = False


if __name__ == '__main__':
    this = Insta()
    this.insta_login()

