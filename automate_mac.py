from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import multiprocessing
import os
from dotenv import load_dotenv

def get_browser(browser_name='edge'):
    """Initialize browser with automatic driver management"""
    browser_name = browser_name.lower()
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        return webdriver.Chrome(options=options)
    elif browser_name == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--no-sandbox')
        return webdriver.Edge(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--no-sandbox')
        return webdriver.Firefox(options=options)
    elif browser_name == 'safari':
        return webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

def search(browser, word):
    """Search for a word on Bing and wait for results to load"""
    # Find the search box
    text_area = browser.find_element(By.ID, 'sb_form_q')
    
    # Clear the search box first
    text_area.clear()
    
    # Alternative clearing method if simple clear() doesn't work
    if text_area.get_attribute('value'):
        text_area.send_keys(Keys.COMMAND + 'a')  # Select all text (use CONTROL for Windows)
        text_area.send_keys(Keys.DELETE)  # Delete selected text
        
    # Enter the new search term
    text_area.send_keys(word)
    text_area.send_keys(Keys.ENTER)
    
    # Wait for the search results to load
    time.sleep(2)

def perform_searches(browser, device, email):
    """Perform searches using trending topics and random words instead of alphabets"""
    import random
    
    # List of trending topics, common search terms, and news topics
    search_terms = [
        # Current events/trends
        "latest news today", "trending topics", "weather forecast",
        "upcoming movies", "new tech gadgets", "popular recipes",
        "stock market today", "sports highlights", "music releases",
        
        # General interest topics
        "travel destinations", "healthy meal ideas", "workout routines",
        "book recommendations", "home improvement tips", "gardening ideas",
        "best smartphone deals", "remote work tips", "streaming shows",
        
        # Questions people search
        "how to make bread", "best laptops 2025", "easy dinner recipes",
        "vacation ideas", "learn coding online", "meditation techniques",
        "home office setup", "electric car reviews", "sustainable living"
    ]
    
    # Shuffle the list for randomization
    random.shuffle(search_terms)
    
    # Determine how many searches to perform based on device
    if device == 'PC':
        # Use the first 36 search terms (or all if less than 36)
        search_count = min(36, len(search_terms))
        for i in range(search_count):
            search(browser, search_terms[i])
    elif device == 'Mobile':
        # Use the first 22 search terms (or all if less than 22)
        search_count = min(22, len(search_terms))
        for i in range(search_count):
            search(browser, search_terms[i])

def process(browser,email,password):
    browser.find_element(By.ID, 'i0116').send_keys(email)
    browser.find_element(By.ID, 'idSIButton9').click()
    time.sleep(5)
    browser.find_element(By.ID, 'i0118').send_keys(password)
    time.sleep(1)
    browser.find_element(By.ID, 'idSIButton9').click()
    time.sleep(5)
    try:
        browser.find_element(By.ID, 'declineButton').click()
        time.sleep(5)
        # browser.find_element(By.ID, 'i0118').send_keys(password)
        # time.sleep(1)
        # browser.find_element(By.ID, 'idSIButton9').click()
        # time.sleep(5)
    except:
        print('Ignore')

def quiz(browser):
    browser.get('https://rewards.bing.com/?ref=rewardspanel')
    main_window = browser.current_window_handle
    try:
        browser.find_element(By.CSS_SELECTOR, 'a[id=signinlinkhero]').click()
        time.sleep(2)
    except:
        pass
    time.sleep(4)
    a = []
    a = browser.find_elements(By.CSS_SELECTOR, 'div[id=daily-sets] mee-card-group.ng-scope.ng-isolate-scope.mobileViewMode div.actionLink.x-hidden-vp1')
    a[0].find_element(By.CSS_SELECTOR, 'span').click()
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    browser.close()
    time.sleep(2)
    browser.switch_to.window(main_window)
    time.sleep(2)
    a[2].find_element(By.CSS_SELECTOR, 'span').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    try:
        browser.find_element(By.CSS_SELECTOR, 'div[id=btoption1]').click()
        time.sleep(2)
    except:
        pass
    browser.close()
    browser.switch_to.window(main_window)
    time.sleep(2)
    a[1].find_element(By.CSS_SELECTOR, 'span').click()
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[1])
    
    try:
        questions = browser.find_element(By.CSS_SELECTOR, 'div.FooterText0.wk_textCenterAlign.b_footnote').text
        # l = (questions[6:]).replace(')','')
        # l = int(l)
        # for i in range(l):
        #     browser.find_element(By.XPATH, "//div[@class='wk_hideCompulsary']/parent::*").click()
        #     time.sleep(1.6)
        #     browser.find_element(By.CSS_SELECTOR, 'input[name=submit]').click()
        #     time.sleep(1.6)
    except:
        print('failed 1')
    
    try:
        try:
            browser.find_element(By.CSS_SELECTOR, 'input[id=rqStartQuiz]').click()
            time.sleep(2)
        except:
            pass
        
        earned_points = int(browser.find_element(By.CSS_SELECTOR, 'span.rqECredits').text)
        total_points = int(browser.find_element(By.CSS_SELECTOR, 'span.rqMCredits').text)
        
        while earned_points < total_points:
            # Get the current state of options
            options = browser.find_elements(By.CSS_SELECTOR, 'input.rqOption')
            for i in range(len(options)):
                try:
                    # Re-fetch options before each click to avoid stale references
                    options = browser.find_elements(By.CSS_SELECTOR, 'input.rqOption')
                    options[i].click()
                    time.sleep(2)
                    
                    # Check if we got it wrong
                    try:
                        wrong = browser.find_element(By.CSS_SELECTOR, 'span.rqwrongAns')
                        if wrong.is_displayed():
                            continue  # Try next option
                    except:
                        # No wrong answer found, means we got it right
                        break
                except Exception as e:
                    print(f'Error clicking option {i}: {e}')
                    continue

            # Re-fetch earned points after trying options
            try:
                earned_points = int(browser.find_element(By.CSS_SELECTOR, 'span.rqECredits').text)
            except:
                # If we can't get points, assume we're done
                break
            time.sleep(2)
    except Exception as e:
        print(f'failed 2: {e}')
    try:
        for i in range(0,11):
            browser.find_element(By.CSS_SELECTOR, 'div[id=rqAnswerOption0]').click()
            time.sleep(5)
    except:
        print('failed 3')

def mobile(email, password, browser_name='edge'):
    browser = get_browser(browser_name)
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 EdgiOS/100.1185.50 Mobile/15E148 Safari/605.1.15'
    })
    browser.get('https://www.bing.com')
    browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d2F18EA8355256B982C9EF89254006A9C&wp=MBI_SSL&lc=1033&CSRFToken=39b09c7a-50b6-4b8f-9974-ac17cd9293c2&aadredir=1')
    time.sleep(8)
    process(browser, email, password)
    perform_searches(browser, 'Mobile', email)

def pc(email, password, arg, browser_name='edge'):
    browser = get_browser(browser_name)
    browser.get('https://www.bing.com')
    browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d030F59AF876A6B3E2C9E4BBE861F6A30&wp=MBI_SSL&lc=1033&CSRFToken=4a56b981-a102-4c54-b092-6004ccaf4248&aadredir=1')    
    time.sleep(6)

    process(browser, email, password)

    if arg and arg[1] == 'alp':
        perform_searches(browser, 'PC', email)
    elif arg and arg[1] == 'quiz':
        quiz(browser)
    else:
        perform_searches(browser, 'PC', email)
        quiz(browser)

def load(email, password, arg, browser_name='edge'):
    if arg:
        if arg[1] == 'pc':
            pc(email, password, arg, browser_name)
        elif arg[1] == 'mobile':
            mobile(email, password, browser_name)
        elif arg[1] in ['quiz', 'alp']:
            pc(email, password, arg, browser_name)
        else:
            pc(email, password, arg, browser_name)
            mobile(email, password, browser_name)
    else:
        pc(email, password, arg, browser_name)
        mobile(email, password, browser_name)

    print('Done')
    try:
        time.sleep(3000)
    except KeyboardInterrupt:
        pass

def load_credentials():
    """Load user credentials from environment variables securely"""
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Get credentials from environment variables
    emails_str = os.environ.get('BING_USER_EMAILS')
    passwords_str = os.environ.get('BING_USER_PASSWORDS')
    
    # Validate credentials exist
    if not emails_str or not passwords_str:
        raise ValueError(
            "Missing credentials in environment variables. "
            "Please set BING_USER_EMAILS and BING_USER_PASSWORDS."
        )
    
    # Split comma-separated credentials into lists
    user_emails = emails_str.split(',')
    user_passwords = passwords_str.split(',')
    
    # Ensure equal number of emails and passwords
    if len(user_emails) != len(user_passwords):
        raise ValueError(
            "Mismatch between number of emails and passwords. "
            "Please ensure each email has a corresponding password."
        )
        
    return user_emails, user_passwords

# Replace hardcoded credentials with environment variables
if __name__ == '__main__':
    t = []
    arg = sys.argv[1:]
    browser_name = arg[0] if arg and arg[0] in ['chrome', 'edge', 'firefox', 'safari'] else 'edge'
    
    # Load credentials from environment variables
    all_user_emails, all_user_passwords = load_credentials()
    
    selected_user_emails = []
    selected_user_passwords = []
    if arg and len(arg) > 2:
        account_indices = arg[2].split(',')
        print(f"Selected accounts: {account_indices}")
        for idx in account_indices:
            index = int(idx) - 1
            if 0 <= index < len(all_user_emails):
                selected_user_emails.append(all_user_emails[index])
                selected_user_passwords.append(all_user_passwords[index])
            else:
                print(f"Warning: Account index {idx} is out of range and will be skipped.")
    else:
        selected_user_emails = all_user_emails
        selected_user_passwords = all_user_passwords

    for i in range(len(selected_user_emails)):
        t.append(multiprocessing.Process(
            target=load, 
            args=(selected_user_emails[i], selected_user_passwords[i], arg, browser_name)
        ))

    for process in t:
        process.start()
    for process in t:
        process.join()
