from PySimpleGUI import PySimpleGUI as sg
import pyautogui as pyg
import sys
import os

while True:
    LocWallet = pyg.locateOnScreen('wallet.png')

    if LocWallet:
        print('ok')
        pyg.click('wallet.png')
        break
    else:
        print('error')
