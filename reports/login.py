from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from reports.send import sendMessage
import time

def loginMail(driver, login, password):

	driver.get('https://account.mail.ru/login')
	other_login = driver.find_element(By.CLASS_NAME, 'ProvidersListItemIcon.ProvidersListItemIconOther.ProvidersListItemIconResponsive')
	other_login.click()
	time.sleep(3)

	email_input = driver.find_element(By.NAME, 'username')
	email_input.send_keys(login)
	email_input.send_keys(Keys.ENTER)
	time.sleep(1)

	password_input = driver.find_element(By.NAME, 'password')
	password_input.send_keys(password)
	password_input.send_keys(Keys.ENTER)
	time.sleep(5)
	