import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random
import time

def test_register():
    path = Service(r'/Users/vivian/PycharmProjects/pytestlab/chromedriver')
    browser = webdriver.Chrome(service=path)
    browser.get('https://www.acy.com/en/open-live-account/')
    time.sleep(2)

    # 帳戶類型
    browser.find_element(By.XPATH, '//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[1]/div/div').click()
    browser.find_element(By.XPATH, '//*[@id="liWrapper"]/li[1]').click()
    time.sleep(random.randint(2, 5))

    # 國家/地區
    browser.find_element(By.XPATH, '//*[@id="input-box"]/div[1]/div').click()
    browser.find_element(By.XPATH, '//*[@id="liWrapper"]/li[8]').click()
    time.sleep(random.randint(2, 5))

    # 稱謂
    browser.find_element(By.XPATH, '//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[3]/div/div').click()
    browser.find_elements(By.XPATH, '//*[@id="liWrapper"]/li[3]')[1].click()
    time.sleep(random.randint(2, 5))

    # lastname
    browser.find_element(By.XPATH, '//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[4]/div/input').send_keys('Han')
    time.sleep(random.randint(2, 5))

    # firstname
    browser.find_element(By.XPATH, '//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[6]/div/input').send_keys('Lu')
    time.sleep(random.randint(2, 5))

    # email
    browser.find_element(By.XPATH, '//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[7]/div/input').send_keys('vian0927@gmail.com')
    time.sleep(random.randint(2, 5))

    # phone
    browser.find_element(By.XPATH, '//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[8]/div/div/div[2]/div/div/input').send_keys('0912345678')
    time.sleep(random.randint(2, 5))

    # submit
    browser.find_element(By.XPATH, '// *[ @ id = "basicInfo"]').submit()
    x = browser.title
    assert x == 'Open A Live Trading Account | Forex Trading | CFDs Trading'

    time.sleep(6)
    browser.close()