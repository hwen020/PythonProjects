#this seems no longer available since the "login" button keeps changing ita xpath.
#but selenium is for automated testing, which is a good tool to learn.


# #no need to log in for automated post
# #use the following link to download geckodriver so that this .py can operate with firefox
# #https://github.com/mozilla/geckodriver/releases
# #make sure your firefox version is compatible(4.7 or higher)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
import time
#
# gecko_path = 'D:\geckodriver\geckodriver.exe'
# # gecko_path = 'path/to/geckodriver'# replace'path/to/geckodriver' with the path to 'geckodriver' executable file
# driver = webdriver.Firefox(executable_path=gecko_path)
#
# driver=webdriver.Firefox()#need to facebook in open firefox
# driver.get('http://facebook.com')
# emailelement=driver.find_element(By.XPATH,'.//*[@id="email"]')#look at the 'how to get XPATH'(firefox)#remember to add a '.' before XPATH
# emailelement.send_keys('9512131639')#enter your own email
# passelement=driver.find_element(By.XPATH,'.//*[@id="pass"]')
# passelement.send_keys('Whr123456,')#enter your own password
#
# elem=driver.find_element(By.XPATH,'.//*[@id="loginbutton"]')
# elem.click()
#
# statuselement=driver.find_element(By.XPATH,"//*[@name='xhpc_message']")
# time.sleep(5)#sec
#
# statuselement.send_keys('Hi there')
# time.sleep(5)
# buttons=driver.find_element_by_tag_name('button')
# time.sleep(5)
# for button in buttons:
#     if button.text=='Post':
#         button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

gecko_path = r'D:\geckodriver\geckodriver.exe'  # 替换为实际的 'geckodriver.exe' 路径
driver = webdriver.Firefox(executable_path=gecko_path)

driver.get('http://facebook.com')
emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailelement.send_keys('9512131639')  # 输入你的邮箱
passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passelement.send_keys('Whr123456,')  # 输入你的密码

elem = driver.find_element(By.XPATH, './/*[@id="u_0_c_pd"]')# //*[@id="loginbutton"]  //*[@id="u_0_5_Au"]  //*[@id="u_0_5_z5"]  //*[@id="u_0_5_v9"]
elem.click()

statuselement = driver.find_element(By.XPATH, "//*[@name='xhpc_message']")
time.sleep(5)

statuselement.send_keys('Hi there')
time.sleep(5)

# 使用 find_elements_by_tag_name 获取所有按钮
buttons = driver.find_elements_by_tag_name('button')

# 遍历按钮，查找包含 'Post' 文本的按钮并点击
for button in buttons:
    if button.text == 'Post':
        button.click()
        break  # 一旦找到并点击按钮，退出循环
