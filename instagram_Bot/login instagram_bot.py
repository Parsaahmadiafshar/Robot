from selenium import webdriver
import os
import time

user = input('Enter user name: ')
passsword = input('Enter password: ')

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path , "chromedriver.exe")

driver = webdriver.Chrome(address)
driver.get('https://instagram.com')
#
time.sleep(5)

user1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
user1.send_keys(user)

passsword1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
passsword1.send_keys(passsword)

login = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
login.click()
