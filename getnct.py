import os
import sys
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import smtplib
from email.mime.text import MIMEText


chrome_options = Options()
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)
driver.get("https://ncts.ie")

while driver.title != 'NCTS Booking':
    print('\nBrowser connected.\nComplete the pre-steps below in the browser first then press enter back here.')
    print('- Accept Cookies\n- Enter Registration and press enter\n- Accept Voluntary Test Warning\n- Confirm your Vehicle Details')
    input('Press Enter here to continue...\t')

Mon = ''
while not Mon or len(Mon) != 3:
    Mon = input('\nType the initial three letters for the expected month\n(ie. Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec):\n')
    Mon = Mon.capitalize()
d1d10 = [' 1st', ' 2nd', ' 3rd', ' 4th', ' 5th', ' 6th', ' 7th', ' 8th', ' 9th', '10th']
d11d20 = ['11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th']
d21d31 = ['21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
dall= d1d10 + d11d20 + d21d31
d_selected = ''
while d_selected not in ['1', '2', '3', '4']:
    d_selected = input('\nWhich period would you prefer?\n-1- 1st to 10th\n-2- 11th to 20th\n-3- 21st to 31st\n-4- the whole month\npress 1/2/3/4 and press enter...\n')
if d_selected == '1':
    date_list = d1d10
elif d_selected == '2':
    date_list = d11d20
elif d_selected == '3':
    date_list = d21d31
elif d_selected == '4':
    date_list = dall
print('\nUser selected:\nMonth:\t' + Mon + '\nPeriod: ')
print(*date_list, sep = ' ')
time.sleep(1)

print('\nDate:\t' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('Message:  Start running...')
# locate to expected NCT centre
if 'Northpoint' not in driver.find_element(By.XPATH, "//span[@id='selectedCentreTitle']").text:
    driver.find_element(By.ID, "showMoreStations").click()
    select_elm = Select(driver.find_element(By.XPATH, "//select[@id='nctCentresDropdown']"))
    select_elm.select_by_visible_text('Northpoint 1 (Exit 4, M50)')
    print('Action:\tChange selected centre to Northpoint 1')
print('Message:  Selected centre is ' + driver.find_element(By.XPATH, "//span[@id='selectedCentreTitle']").text)

i = 0
while i == 0:
    date = driver.find_elements(By.XPATH, "//label[@class='booking-available-slot booking-available-slot--arrow']")
    for d in date:
        if Mon in d.text:
            selected_d = d.text.replace('\n',' ')
            print('\nDate:\t' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print('Result:\tFound available MONTH ' + selected_d)
            # change below for expected dates
            for date_i in date_list:
                if date_i in selected_d:
                    d.click()
                    centre = driver.find_element(By.XPATH, "//span[@id='selectedCentreTitle']").text
                    driver.switch_to.window(driver.current_window_handle)
                    driver.maximize_window()
                    print('\nDate:\t' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    print('Result:\tFound available DATE ' + selected_d)
                    print('Result:\tLocated centre ' + centre)
                    # email alert
                    # put in your email user.name
                    mail_user = 'address@gmail.com'
                    # create a Gmail app password for your Gmail account
                    # https://myaccount.google.com/apppasswords
                    # put generated password in $mail_pass
                    mail_pass = '' 
                    # put in your email address
                    sender = 'address@gmail.com'  
                    # put in email-to address
                    receivers = 'address@gmail.com'
                    # content
                    message = MIMEText(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n' + selected_d + '\n' + centre + '\nPLEASE SELECT THE TIME AND CONFIRM THE BOOKING AS SOON AS POSSIBLE\n','plain','utf-8')    
                    # put in email title
                    message['Subject'] = 'NCT Appointment Found' 
                    message['From'] = sender     
                    message['To'] = receivers  
                    try:
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                            smtp_server.login(mail_user,mail_pass) 
                            smtp_server.sendmail(sender,receivers,message.as_string()) 
                        print('Message:  Email sent successfully.')
                    except smtplib.SMTPException as e:
                        print('Alert:\tEmail sent failed\n\t',e)
                    input('Alert:\tDO NOT CLOSE THIS WINDOW OR PRESS ANYTHING UNTIL YOU COMPLETE THE BOOKING.')
                    sys.exit()
            print('Message:  Date not expected ' + d.text.replace('\n',' '))
            i += 1
        else:
            i += 1
        if i == 5:
            try:
                driver.find_element(By.XPATH, "//button[@class='owl-next']").click()
                time.sleep(0.2)
                driver.find_element(By.XPATH, "//button[@class='owl-next']").click()
                time.sleep(0.2)
                driver.find_element(By.XPATH, "//button[@class='owl-next']").click()
                time.sleep(0.2)
                driver.find_element(By.XPATH, "//button[@class='owl-next']").click()
                time.sleep(0.2)
                driver.find_element(By.XPATH, "//button[@class='owl-next']").click()
                time.sleep(0.2)
                i = 0
            except:
                driver.find_element(By.ID, "showMoreStations").click()
                select_elm = Select(driver.find_element(By.XPATH, "//select[@id='nctCentresDropdown']"))
                if driver.find_element(By.XPATH, "//span[@id='selectedCentreTitle']").text == 'Northpoint 1 (Exit 4, M50)':
                    select_elm.select_by_visible_text('Northpoint 2 (Exit 4, M50)')
                    print('\nDate:\t' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    print('Action:\tChange selected centre to Northpoint 2')
                    time.sleep(0.2)
                else:
                    select_elm.select_by_visible_text('Northpoint 1 (Exit 4, M50)')
                    print('\nDate:\t' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    print('Action:\tChange selected centre to Northpoint 1')
                    time.sleep(0.2)
                i = 0
                break
