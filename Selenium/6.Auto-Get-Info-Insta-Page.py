from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from colorama import Fore , Style
from password import username , password



page = input("Please Enter Your Instagram Page :").split(' ')
addresss = os.path.abspath(__file__)
addresss = os.path.dirname(addresss)
addresss = os.path.join(addresss , 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=addresss)
driver.maximize_window()
driver.get('https://instagram.com')

usr = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
usr.send_keys(username)
pas = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pas.send_keys(password + Keys.ENTER)
time.sleep(3)

for i in page:
    if '#' == i[0]:
        driver.get(f'https://instagram.com/explore/tags/{i[1:]}/')
        time.sleep(3)
        post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/div[2]/span/span').text
    else:
        driver.get(f'https://instagram.com/{i}/')
        time.sleep(3)
        post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').text
        followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
        following = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
    os.system('cls')
    time.sleep(1)
    print()
    print(Fore.GREEN + 'Page Name :' + Fore.YELLOW + i , '\n')
    print(Fore.YELLOW + 'Post Number :' + Fore.RED + str(post))
    try:
        print(Fore.YELLOW + 'Follower Number :' + Fore.RED + str(followers))
        print(Fore.YELLOW + 'Following Number :' + Fore.RED + str(following))
    except:
        continue
    finally:
        print()
