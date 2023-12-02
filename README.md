**getNCT** - Auto refresh and check your expected NCT period

---

Usage: 

Simply double click **getnct.py** in the cloned repo.

User needs to config the script for expected 2x centres, and the email info once for sending available date message. 

The script will ask you for expected month and date period.

**NB*** During the auto check, if the script find an available date, it will alert you by maxmising the browser window and emailing you. While it will NOT confirm the booking as you need to select the time and pay for the booking. Therefore, please proceed the rest of the steps as soon as possible after you receive the message.

Press `control + c` to terminate script if you need to change selected month, date, centre, email.


---

**pre-setup**

- install Python (of course)
- install Google Chrome
- install below module from Pypi
    - pip install selenium
    - pip install webdriver_manager


**config getnct.py**

*Pay attention to all commented area (line with #)*

- change expected NCT centres
    - default 2x NCT centres are 'Northpoint 1 (Exit 4, M50)' and 'Northpoint 2 (Exit 4, M50)'
    - access to the centre list and change the centres you want
    - the lines with 'Northpoint 1 (Exit 4, M50)' are line 53, 121, 127 for functioning, and line 54, 129 printing message
    - the lines with 'Northpoint 2 (Exit 4, M50)' are line 122, for functioning, and line 124 for printing message

- change email inforamtion starting from line 75
    - change all 'address@gmail.com' in the script to your email address
    - update $mail_pass following the comment lines above it
    - (the password is different from the password you used to login, etc.)

---

**Terminal Layout**
```````
DevTools listening on ...

Browser connected.
Complete the pre-steps below in the browser first then press enter back here.
- Accept Cookies
- Enter Registration and press enter
- Accept Voluntary Test Warning
- Confirm your Vehicle Details
Press Enter here to continue...

Type the initial three letters for the expected month
(ie. Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec):
# May

Which period would you prefer?
-1- 1st to 10th
-2- 11th to 20th
-3- 21st to 31st
-4- the whole month
press 1/2/3/4 and press enter...
# 3

User selected:
Month:  May
Period:
21st 22nd 23rd 24th 25th 26th 27th 28th 29th 30th 31st

Date:   2023-12-02 15:09:53
Message:  Start running...
Action: Change selected centre to Northpoint 1
Message:  Selected centre is Northpoint 1 (Exit 4, M50)

Date:   2023-12-02 15:43:15
Result: Found available MONTH Monday 20th May
Message:  Date not expected Monday 20th May

Date:   2023-12-02 15:43:22
Result: Found available MONTH Tuesday 21st May

Date:   2023-12-02 15:43:22
Result: Found available DATE Tuesday 21st May
Result: Located centre Northpoint 1 (Exit 4, M50)
Message:  Email sent successfully.
Alert:  DO NOT CLOSE THIS WINDOW OR PRESS ANYTHING UNTIL YOU COMPLETE THE BOOKING.
```````