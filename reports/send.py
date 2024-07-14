from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def sendMessage(driver, recep, title, body):
	new_message = driver.find_element(By.CLASS_NAME, 'compose-button__wrapper')
	new_message.click()
	time.sleep(2)

	recepient = driver.find_element(By.CLASS_NAME, 'container--H9L5q.size_s--3_M-_')
	recepient.send_keys(recep)

	title_message = driver.find_element(By.NAME, 'Subject')
	title_message.send_keys(title)

	body_message = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[4]/div/div/div[2]/div[1]/div[2]')
	body_message.send_keys(body)

	button_send = driver.find_element(By.CLASS_NAME, 'vkuiButton__content')
	button_send.click()

	time.sleep(2)
	close_wind = driver.find_element(By.CLASS_NAME, 'button2.button2_has-ico.button2_has-ico-s.button2_close.button2_pure.button2_short.button2_hover-support')
	close_wind.click()


