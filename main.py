import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from datetime import datetime
from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from telethon import TelegramClient

mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 7.3.0; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

def get_mail(browser_1 , mail):
    tries = 50
    i = 0
    while tries > 0 :
        browser_1.get("https://tempmail.email/")
        browser_1.implicitly_wait(5)
        time.sleep(1)
        path = '/html/body/div[2]/div/div[1]/div[3]/div/div[2]'
        browser_1.implicitly_wait(5)
        element = browser_1.find_elements_by_xpath(path)
        browser_1.implicitly_wait(5)
        i += 1
        if element[0].text != "":
            mail = element[0].text
            tries = 0
            if re.search('gotgel', mail):
                print("gotgel again!")
                browser_1.close()
                browser_1 = webdriver.Chrome(executable_path=r"C:\chromedriver.exe",options=chrome_options)
                browser_1, mail = get_mail(browser_1, mail)
        tries -= 1
    return browser_1, mail

def instagram_worker(browser_2, mail):
    browser_2.get('https://www.instagram.com')
    browser_2.implicitly_wait(10)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div/button").click()
    browser_2.implicitly_wait(10)
    time.sleep(3)
    browser_2.get('https://www.instagram.com/accounts/signup/email')
    browser_2.implicitly_wait(10)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[2]/div[3]/div/label/input").send_keys(mail)
    browser_2.implicitly_wait(10)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[3]/button").click()
    return browser_2

def conform_code_mail(browser_1,confirm_code):
    confirm_code = ""
    while(confirm_code == ''):
        browser_1.implicitly_wait(10)
        time.sleep(1)
        code = browser_1.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div[4]/div[2]/div[2]/div/div[3]/div[2]")
        for codes in code:
            confirm_code = codes.text
        browser_1.get("https://tempmail.email/")
    res = re.sub("\D", "", confirm_code)
    confirm_code = res
    return browser_1 , confirm_code

def signup(browser_2,confirm_code):
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[1]/div[3]/div/label/input").send_keys(confirm_code)
    browser_2.implicitly_wait(10)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[2]/button").click()
    browser_2.implicitly_wait(5)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[1]/div[3]/div/label/input").send_keys("Devinso1")
    browser_2.implicitly_wait(5)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[1]/div[4]/div/label/input").send_keys("Estkra@#")
    browser_2.implicitly_wait(5)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[2]/button").click()
    browser_2.implicitly_wait(5)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[1]/div[4]/div/div/span/span[3]/select/option[17]").click()
    browser_2.implicitly_wait(5)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[1]/div[4]/div/div/span/span[2]/select/option[5]").click()
    browser_2.implicitly_wait(5)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[1]/div[4]/div/div/span/span[1]/select/option[2]").click()
    browser_2.implicitly_wait(5)
    time.sleep(1)
    browser_2.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[2]/button").click()
    return browser_2

def main():
    mail = ""
    confirm_code = ""

    browser_1 = webdriver.Chrome(executable_path=r"/home/admin-u3f/Desktop/insta_creator/chromedriver",
                                 options=chrome_options)
    browser_1, mail = get_mail(browser_1, mail)
    browser_2 = webdriver.Chrome(executable_path=r"/home/admin-u3f/Desktop/insta_creator/chromedriver",
                                 options=chrome_options)
    browser_2 = instagram_worker(browser_2 , mail)
    browser_1 , confirm_code = conform_code_mail(browser_1,confirm_code)
    browser_2 = signup(browser_2,confirm_code)
    browser_2.delete_all_cookies()
    browser_1.delete_all_cookies()
    browser_2.close()
    browser_1.close()

while(True):
    try:
        main()
    except:
        print("error")

