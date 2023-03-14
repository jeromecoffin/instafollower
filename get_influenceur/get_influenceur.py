import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep,strftime
from random import randint
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Change below to your own folder path
chrome_driver_binary = '/Users/jeromecoffin/git_repo/instafollower/get_influenceur/chromedriver_mac64/chromedriver'  
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Chromium.app/Contents/MacOS/Chromium"
sleep(2)
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher') 
sleep(3)

# accept cookies if banner is present
cookies_banner = driver.find_elements(By.XPATH, '//button[text()="Autoriser les cookies essentiels et optionnels"]')
if cookies_banner:
    cookies_banner[0].click()

sleep(5)

username = driver.find_element(by='name', value='username')
username.send_keys('hari.responsable')
#username.send_keys('french_anatra')


password = driver.find_element(by='name', value='password')
password.send_keys('zipxi1-fasrib-deDdah')
#password.send_keys('en mode bg 1998')

sleep(5)

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
login_button.click()

sleep(3)

notification_banner = driver.find_elements(By.XPATH, '//button[text()="Plus tard"]')
if notification_banner:
    notification_banner[0].click()
sleep(3)

identifiant_banner = driver.find_elements(By.XPATH, '//button[text()="Plus tard"]')
if identifiant_banner:
    identifiant_banner[0].click()
sleep(3)

prev_user_list = [] 
new_tracked = []
new_tracked_url=[]
tag = -1

hashtag_list = ['moderesponsable', 'modedurable']
for hashtag in hashtag_list:
    tag += 1
    driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    for i in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
    hrefs = driver.find_elements(By.TAG_NAME, 'a')
    pic_hrefs = [elem.get_attribute('href') for elem in hrefs if '.com/p/' in elem.get_attribute('href')]
    for pic_href in pic_hrefs:
        driver.get(pic_href)
        sleep(5)
        try:
            username = driver.find_element(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _acan _acao _acat _acaw _aj1- _a6hd"]').text
            new_tracked.append(username) 
            new_tracked_url.append('https://www.instagram.com/'+username+'/')
        except:
            username = driver.find_element(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _acan _acao _acat _acaw _aj1- _a6hd"]').text
            new_tracked.append(username)
            new_tracked_url.append('https://www.instagram.com/'+username+'/')
        sleep(randint(5,15))

    dic={'username':new_tracked,'user_url':new_tracked_url}
    updated_user_df = pd.DataFrame(dic)
    updated_user_df.to_csv(hashtag+'_{}_users_list.csv'.format(strftime("%Y%m%d")))