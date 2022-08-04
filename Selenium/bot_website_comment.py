from selenium import webdriver
import os
import time

path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, "chromedriver.exe")

driver = webdriver.Chrome(address)
driver.get('https://techone24.ir')
#
time.sleep(5)

blog = driver.find_element_by_xpath('/html/body/div[1]/header/div/section/div/div/div/header/div/div[2]/div/div[2]/div/nav[1]/ul/li[4]/a')
blog.click()
time.sleep(3)
article = driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/div[4]/article/a[2]/h3')
article.click()
time.sleep(3)
comment = driver.find_element_by_xpath('//*[@id="comment"]')
comment.send_keys("عالی بود")
time.sleep(2)

comment = driver.find_element_by_xpath('//*[@id="author"]')
comment.send_keys('bot_python*')
time.sleep(2)

comment = driver.find_element_by_xpath('//*[@id="email"]')
comment.send_keys('bot_python*@gmail.com')
time.sleep(2)


Apply = driver.find_element_by_xpath('//*[@id="submit"]')
Apply.click()

