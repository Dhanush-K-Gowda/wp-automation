import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

csv_path = 'table.csv'
df = pd.read_csv(csv_path)
#print(df)


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Please scan the QR code to log in.")
time.sleep(20)

message='this is python'
for phone_number in df['Phone']:
            print("Sending msg to",phone_number)
            link = f'https://web.whatsapp.com/send/?phone={phone_number}&text={message}'
            driver.get(link)
            time.sleep(20)

            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(3)
          #  pywhatkit.sendwhatmsg(phone_number, "Hi", ,)

