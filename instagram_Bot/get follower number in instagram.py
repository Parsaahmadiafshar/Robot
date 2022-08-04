from selenium import webdriver
import os
import time

user = input('Enter user name: ')
passsword = input('Enter password: ')
ID = input('Enter ID: ')
path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, "chromedriver.exe")

driver = webdriver.Chrome(address)
driver.get('https://instagram.com')
#
time.sleep(5)

user1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
user1.send_keys(user)
time.sleep(3)
passsword1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
passsword1.send_keys(passsword)

login = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
login.click()

time.sleep(3)

ID1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input')
ID1.send_keys(ID)
ID1.click(ID)
time.sleep(2)

followers = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div").text
print(f'the number of followers is {followers}')