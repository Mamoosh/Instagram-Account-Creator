import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define mobile emulation settings
mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 7.3.0; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

def get_mail(browser):
    for _ in range(50):
        browser.get("https://tempmail.email/")
        time.sleep(1)
        element = browser.find_elements_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div[2]')
        if element[0].text != "" and not re.search('gotgel', element[0].text):
            return element[0].text
    return None

def instagram_worker(browser, mail):
    browser.get('https://www.instagram.com')
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div/button").click()
    time.sleep(3)
    browser.get('https://www.instagram.com/accounts/signup/email')
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[2]/div[3]/div/label/input").send_keys(mail)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div[3]/button").click()
    return browser

def conform_code_mail(browser):
    while True:
        time.sleep(1)
        code = browser.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div[4]/div[2]/div[2]/div/div[3]/div[2]")
        confirm_code = [codes.text for codes in code if codes.text]
        if confirm_code:
            return re.sub("\D", "", confirm_code[0])
        browser.get("https://tempmail.email/")

def signup(browser, confirm_code):
    # ... rest of your signup code ...
    return browser

def main():
    browser_1 = webdriver.Chrome(executable_path=r"/home/admin-u3f/Desktop/insta_creator/chromedriver", options=chrome_options)
    mail = get_mail(browser_1)
    if mail is None:
        print("Failed to get mail")
        return

    browser_2 = webdriver.Chrome(executable_path=r"/home/admin-u3f/Desktop/insta_creator/chromedriver", options=chrome_options)
    browser_2 = instagram_worker(browser_2 , mail)
    confirm_code = conform_code_mail(browser_1)
    browser_2 = signup(browser_2, confirm_code)
    browser_2.delete_all_cookies()
    browser_1.delete_all_cookies()
    browser_2.close()
    browser_1.close()

while True:
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
