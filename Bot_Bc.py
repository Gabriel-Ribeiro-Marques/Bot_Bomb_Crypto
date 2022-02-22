from PySimpleGUI import PySimpleGUI as sg
import pyautogui as pyg
import os
import sys

archive = open('Config_bot.txt', 'r')
listconfig = archive.readlines()
print(listconfig)
tdmin = 1800
hrssmn = 7000

class StartingBot():

    def __init__(self):
        print('funcionando')
        StartingBot.FirstSteps(self)

        #print(f'{listconfig[1]}{listconfig[2]}')
        #pyg.moveTo(int(listconfig[1]), int(listconfig[2]))

    def FirstSteps(self):
        pyg.sleep(1)
        pyg.moveTo(int(listconfig[1]), int(listconfig[2]), duration=2)
        pyg.click()
        pyg.sleep(1)
        StartingBot.LoopEvents(self)

    def LoopEvents(self):
        pyg.moveTo(int(listconfig[4]), int(listconfig[5]), duration=2)
        pyg.sleep(1)
        pyg.click()
        pyg.sleep(1)
        pyg.click()
        pyg.moveTo(int(listconfig[7]), int(listconfig[8]), duration=2)
        pyg.click()
        pyg.sleep(1)
        pyg.moveTo(int(listconfig[13]), int(listconfig[14]), duration=2)
        pyg.sleep(1)
        pyg.click()
        pyg.sleep(3)
        pyg.click()
        sg.popup_auto_close('you Have 30 min free')
        pyg.sleep(tdmin)
        sg.popup_auto_close('re back')
        pyg.sleep(1)
        pyg.moveTo(int(listconfig[4]), int(listconfig[5]), duration=2)
        pyg.click()
        pyg.sleep(1)
        pyg.click()
        pyg.moveTo(int(listconfig[10]), int(listconfig[11]), duration=2)
        pyg.click()
        pyg.sleep(1)
        pyg.moveTo(int(listconfig[13]), int(listconfig[14]), duration=2)
        pyg.click()
        pyg.sleep(1)
        pyg.click()
        pyg.sleep(1)
        sg.popup_auto_close('you Have 30 min free')
        pyg.sleep(hrssmn)
        sg.popup_auto_close('re back')
        pyg.sleep(1)
        #StartingBot.ReLogin(self)


    def ReLogin(self):
        pyg.click()
        pyg.hotkey('shift','f5')
        while True:
            LocWallet = pyg.locateOnScreen('wallet.png')
            if LocWallet:
                pyg.click('wallet.png', duration=2)
                while True:
                    locass = pyg.locateOnScreen('login.png')
                    errorlogin = pyg.locateOnScreen('oko.png')
                    if pyg.locateOnScreen('login.png'):
                        print('err')
                        pyg.click('login.png', duration=2)
                        pyg.sleep(10)
                        break
                    elif errorlogin:
                        print('pip')
                        pyg.click('oko.png', duration=2)
                        break
                    else:
                        break
            else:
                continue


    def TimeCommun(self):
        pass
