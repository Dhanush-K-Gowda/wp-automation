import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import pywhatkit
from selenium.webdriver.common.keys import Keys
import time
import keyboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

csv_path = 'table.csv'
df = pd.read_csv(csv_path)
#print(df)


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Please scan the QR code to log in.")
time.sleep(20)

message='Hello we invite you to CTF organised by SARK'
for phone_number in df['Phone']:
            pywhatkit.sendwhats_image(f'{phone_number}', "hello.jpg")
            print("Sending msg to",phone_number)
            link = f'https://web.whatsapp.com/send/?phone={phone_number}&text={message}'
            driver.get(link)
            time.sleep(30)
            
            plbtn='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'
            driver.find_element("xpath",plbtn).click()
            time.sleep(1) 

            imbtn='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/span'
            driver.find_element("xpath",imbtn).click()
            time.sleep(1)

            keyboard.write('img.jpg')
            time.sleep(2)

            keyboard.press_and_release('enter')
            time.sleep(2)

            sndbtn='//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'
            driver.find_element("xpath",sndbtn).click()
            time.sleep(5)

