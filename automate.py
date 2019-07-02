from selenium import webdriver
import time
import string
import threading
import getpass


def search(browser,word):
    text_area = browser.find_element_by_id('sb_form_q')
    text_area.send_keys(word)
    try:
        browser.find_element_by_id('sb_form_go').click()
    except:
        browser.find_element_by_id('sbBtn').click()
    time.sleep(2)

def next(browser):
    browser.find_element_by_id('idSIButton9').click()
    time.sleep(2)

def process(browser,email,password):
    browser.find_element_by_id('i0116').send_keys(email)
    next(browser)

    browser.find_element_by_id('i0118').send_keys(password)
    next(browser)

    for i in string.ascii_lowercase[:26]:
        search(browser,i)
    for i in string.ascii_uppercase[:5]:
        search(browser,i)

def load(email,password):
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path = 'chromedriver')
    # browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')    
    browser.get('https://www.bing.com')
    time.sleep(6)

    sign_in = browser.find_element_by_id('id_s')
    sign_in.click()
    time.sleep(8)

    process(browser,email,password)

    # browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1)"')
    browser = webdriver.Chrome(executable_path = 'chromedriver', chrome_options=chrome_options)
    browser.get('https://www.bing.com')

    time.sleep(8)

    browser.find_element_by_id('mHamburger').click()
    time.sleep(2)


    browser.find_element_by_id('hb_s').click()
    time.sleep(4)

    process(browser,email,password)

    browser.quit()


user_email = []
user_pass = []
print('Enter number of accounts you want to automate')
n = int(input())
for i in range(n):
    print('Enter email id :')
    user_email.append(input())
    print('Enter password for ' + str(user_email[i]))
    user_pass.append(getpass.getpass())

t = []
for i in range(3):
    t.append(threading.Thread(target=load, args=(user_email[i],user_pass[i],)))
for i in t:
    i.start()
