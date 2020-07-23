# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time
import csv


def sendkey_by_id(elem, value):
    item = browser.find_element_by_id(elem)
    item.send_keys(value)


driver_path = "chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
browser.page_source.encode('utf_8_sig')
WebDriverWait(browser, 10)
main_window = browser.current_window_handle

# Wait for login
ec.visibility_of_element_located(locator=('ID', 'username'))
# Try Login
try:
    sendkey_by_id('username', 'YOUR_LINKEDIN_LOGIN')
    sendkey_by_id('password', 'YOUR_LINKEDIN_PASSWORD')
    browser.find_element_by_css_selector('div#app__container button[type="submit"]').click()
    time.sleep(5)
except NoSuchWindowException:
    print ('%s Error:') % ('NoSuchWindowException')

# Go to contact detail page
time.sleep(3)
browser.get("https://www.linkedin.com/in/sercanerhan/detail/contact-info/")
time.sleep(3)
element= browser.find_element_by_xpath("//*[contains(@href,'@')]")
email_address =  (element.get_attribute('HREF')).replace('mailto:','')

# Save the result 
f = open('email_address.txt','w')
f.write(email_address)
f.close()

# Close the browser
browser.close()