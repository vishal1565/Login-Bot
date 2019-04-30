from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from getpass import getpass

def printUse():
    print("Usage: python automateLogin.py -[fb/gmail]")
    print("Eg: python automateLogin.py -fb")
    print("Eg: python automateLogin.py -gmail")

if len(sys.argv)==2:
    email = input("Enter Email: ")
    psd = getpass("Enter Password: ")

    if sys.argv[1]=='-gmail':
        try:
            print("Now logging you in your gmail account..\n")
            driver = webdriver.Chrome()
            driver.get("https://mail.google.com")
            driver.find_element_by_id('identifierId').send_keys(email)
            driver.find_element_by_id('identifierNext').click()
            sleep(2)
            driver.find_element_by_name('password').send_keys(psd)
            driver.find_element_by_id('passwordNext').click()
            driver.maximize_window()
        except:
            print("An Error Occurred..")
    elif sys.argv[1]=='-fb':
        try:
            print("Logging you to your facebook id..\n")
            driver = webdriver.Chrome()
            driver.get("https://facebook.com")
            driver.find_element_by_id('email').send_keys(email)
            driver.find_element_by_id('pass').send_keys(psd)
            driver.find_element_by_id('loginbutton').click()
            driver.maximize_window()
        except:
            print("An Error Occurred..")
    else:
        print("Unsupported website")
else:
    printUse()