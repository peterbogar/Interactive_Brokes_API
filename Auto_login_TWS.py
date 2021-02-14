# MYS: 1440x900
# OBR: 2880x1800

import pyautogui
import os
import time
import privat

# Otvor TWS
os.system('open /Users/'+privat.macos_user+'/Applications/Trader\ Workstation/Trader\ Workstation.app')

# Pausa na nacitanie
time.sleep(15)

# Najde polohu okna
logo = pyautogui.locateOnScreen('ibkr_logo.png', confidence=0.9)

# Ak najdes okno
if logo:
    logo_y = logo.top / 2
    logo_x = logo.left / 2

    # Klikni na "Paper trading"
    pyautogui.moveTo(logo_x + 400, logo_y + 160)
    pyautogui.click()

    # Najdi pole "user name"
    user_name = pyautogui.locateOnScreen('user_name.png', confidence=0.9)
    user_name_y = user_name.top / 2
    user_name_x = user_name.left / 2
    pyautogui.moveTo(user_name_x + 50, user_name_y + 15)
    pyautogui.click()
    pyautogui.typewrite(privat.tws_user_name, interval=0.1)

    # Najdi pole user "password"
    password = pyautogui.locateOnScreen('password.png', confidence=0.9)
    password_y = password.top / 2
    password_x = password.left / 2
    pyautogui.moveTo(password_x + 50, password_y + 15)
    pyautogui.click()
    pyautogui.typewrite(privat.tws_password, interval=0.1)

    # Enter
    pyautogui.press('enter')

    print('TWS loading...')

else:
    print('Nenasiel som okno!')
