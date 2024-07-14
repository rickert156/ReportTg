from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
from reports.login import loginMail
from reports.send import sendMessage
from telegram import telegram
from template import title, body


driver = webdriver.Chrome()
driver.maximize_window()

account = 'accounts.csv'
def main():
	with open(account, 'r') as data_read:
		number_account = 0
		for row in csv.DictReader(data_read):
			number_account+=1
			login = row['login']
			password = row['password']
			print(f'Аккаунт {number_account} [{login}]')
			# owner(driver)
			loginMail(driver, login, password)
			number_send=0
			for tg in telegram:
				number_send+=1
				try:
					sendMessage(driver, tg, title, body)
					print(f'Отпавлено на {tg}')
				except Exception as ex:
					print(f'Ошбка при попытке отправить письмо\nError {ex}')

if __name__ == '__main__':
	main()