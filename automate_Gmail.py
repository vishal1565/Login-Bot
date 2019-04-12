from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

email = input("Enter Email: ")
psd = input("Enter Password: ")

print("Now logging you in your gmail account..\n")
driver = webdriver.Chrome()
driver.get("https://mail.google.com")
driver.find_element_by_id('identifierId').send_keys(email)
driver.find_element_by_id('identifierNext').click()
sleep(2)
driver.find_element_by_name('password').send_keys(psd)
driver.find_element_by_id('passwordNext').click()
driver.maximize_window()