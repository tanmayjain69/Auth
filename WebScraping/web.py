from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#url=input()

def hrLogin(username,password):
    browser = webdriver.Chrome(r"C:\Users\Arnav\PycharmProjects\Auth\chromedriver")
    url="https://www.hackerrank.com/auth/login"
    browser.get(url)
    email=browser.find_element_by_id("input-1")
    email.send_keys(username)
    passw=browser.find_element_by_id("input-2")
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)
    return

#elem=browser.find_element_by_link_text('Log in')
#elem.click()

    
def fbLogin(username,password):
    browser = webdriver.Chrome(r"C:\Users\Arnav\PycharmProjects\Auth\chromedriver")
    url="https://www.facebook.com/"
    browser.get(url)
    email=browser.find_element_by_id("email")
    email.send_keys(username)
    passw=browser.find_element_by_id("pass")
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)
    return

def lmsLogin(username,password):
    browser = webdriver.Chrome(r"C:\Users\Arnav\PycharmProjects\Auth\chromedriver")
    url="http://lms.bennett.edu.in/"
    browser.get(url)
    email=browser.find_element_by_id("inputName")
    email.send_keys(username)
    passw=browser.find_element_by_id("inputPassword")
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)
    return

