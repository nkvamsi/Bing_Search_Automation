# from selenium import webdriver
import time
import string
import threading
import getpass
import os
from msedge.selenium_tools import Edge, EdgeOptions

def search(browser,word):

    text_area = browser.find_element_by_id('sb_form_q')
    text_area.send_keys(word)
    try:
        browser.find_element_by_id('sb_form_go').click()
    except:
        try:
            browser.find_element_by_id('sbBtn').click()
        except:
            browser.find_element_by_css_selector('label[class]').click()
    time.sleep(2)


def alphabets(browser,device):
    
    if device == 'PC':
        for i in string.ascii_lowercase[:10]:
            search(browser,i)
        for i in string.ascii_uppercase[:26]:
            search(browser,i)
    elif device == 'Mobile':
        for i in string.ascii_uppercase[:22]:
            search(browser,i)

def process(browser,email,password):

    browser.find_element_by_id('i0116').send_keys(email)

    browser.find_element_by_id('idSIButton9').click()
    time.sleep(4)
    browser.find_element_by_id('i0118').send_keys(password)
    time.sleep(1)
    browser.find_element_by_id('idSIButton9').click()
    time.sleep(5)
    try:
        browser.find_element_by_id('idBtn_Back').click()
        time.sleep(5)
    except:
        pass
    try:
        browser.find_element_by_css_selector('div[id=msaTile]').click()
    except:
        pass

def quiz(browser):
    # Testing
    browser.get('https://account.microsoft.com/rewards/?ref=bingflyout&refd=www.bing.com')
    main_window = browser.current_window_handle
    try:
        browser.find_element_by_css_selector('a[id=signinlinkhero]').click()
        time.sleep(2)
    except:
        pass
    time.sleep(4)
    a=[]
    a = browser.find_elements_by_css_selector('div[id=daily-sets] mee-card-group.ng-scope.ng-isolate-scope.mobileViewMode div.actionLink.x-hidden-vp1')
    a[0].find_element_by_css_selector('span').click()
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    browser.close()
    time.sleep(2)
    browser.switch_to.window(main_window)
    time.sleep(2)
    a[2].find_element_by_css_selector('span').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    try:
        browser.find_element_by_css_selector('div[id=btoption1]').click()
        time.sleep(2)
    except:
        pass
    browser.close()
    browser.switch_to.window(main_window)
    time.sleep(2)
    a[1].find_element_by_css_selector('span').click()
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[1])
    try:
        questions = browser.find_element_by_css_selector('div.FooterText0.wk_textCenterAlign.b_footnote').text
        l = (questions[6:]).replace(')','')
        l = int(l)
        for i in range(l):
            browser.find_element_by_xpath("//div[@class='wk_hideCompulsary']/parent::*").click()
            time.sleep(1.6)
            browser.find_element_by_css_selector('input[name=submit]').click()
            time.sleep(1.6)
    except:
        print('failed 1')
    # # try:
    # #     input[id=rqStartQuiz]
    # #     //input[@class='rqOption correctAnswer']/@value
    # except:
    #     print('failed 1')
    try:
        browser.find_element_by_css_selector('input[id=rqStartQuiz]').click()
        time.sleep(2)
        l = browser.find_element_by_css_selector('span.rqPoints').text # 2nd pos
        l = int(l[2])
        for i in range(100):
            selections = browser.find_elements_by_css_selector('div[iscorrectoption=True]')
            # print(len(selections))
            for j in range(int(len(selections))):
                try:
                    selections[j].click()
                    # selections[j].find_element_by_css_selector('div.bt_cardText').click()
                    time.sleep(2)
                except:
                    pass
    except:
        print('failed 2')

    #------------------------------------------------------------

def mobile(email,password):
    # chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1)"')
    # browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
    # browser = webdriver.Chrome(executable_path = 'chromedriver', chrome_options=chrome_options)
    browser = Edge(executable_path="/Users/krishna/Documents/bing/driver",capabilities=desired_cap)
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 EdgiOS/100.1185.50 Mobile/15E148 Safari/605.1.15'})
    browser.get('https://www.bing.com')
    browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d2F18EA8355256B982C9EF89254006A9C&wp=MBI_SSL&lc=1033&CSRFToken=39b09c7a-50b6-4b8f-9974-ac17cd9293c2&aadredir=1')
    # time.sleep(4)
    # browser.get('https://www.bing.com')
    time.sleep(8)

    # browser.find_element_by_id('mHamburger').click()    
    # time.sleep(4)


    # browser.find_element_by_id('hb_s').click()
    # time.sleep(4)

    process(browser,email,password)

    alphabets(browser,'Mobile')

def pc(email,password):
    browser = Edge(executable_path="/Users/krishna/Documents/bing/driver", capabilities=desired_cap)
    # browser = webdriver.Chrome(executable_path = 'chromedriver', chrome_options=chrome_options)
    # browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')   
    # browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": '    Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/104.0.1293.70'})    
    browser.get('https://www.bing.com')
    browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d030F59AF876A6B3E2C9E4BBE861F6A30&wp=MBI_SSL&lc=1033&CSRFToken=4a56b981-a102-4c54-b092-6004ccaf4248&aadredir=1')    
    time.sleep(6)

    # try:
    #     sign_in = browser.find_element_by_id('id_s')
    # except:
    #     sign_in = browser.find_element_by_id('id_a')
    # sign_in.click()
    # time.sleep(15)

    process(browser,email,password)

    alphabets(browser,'PC')

    quiz(browser)

def load(email,password):
    
    pc(email,password)
    mobile(email,password)

desired_cap = {}
chrome_options = EdgeOptions()
chrome_options.use_chromium = True
chrome_options.add_argument('--no-sandbox')

user_email = ['nkvamsi97@gmail.com','kchaitanya863@gmail.com','nlumia0@outlook.com','nlumia2@outlook.com']
user_pass = ['krishna!','Kchaitanya123','krishna!','krishna!']

# user_email = ['nlumia0@outlook.com','nlumia2@outlook.com']
# user_pass = ['krishna!','krishna!']

# user_email = [user_email[0]]
# user_pass = [user_pass[0]]

t = []
for i in range(len(user_email)):
    t.append(threading.Thread(target=load, args=(user_email[i],user_pass[i],)))

for i in t:
    i.start()
for i in t:
    i.join()

print('Done')
time.sleep(300)