from PySimpleGUI import PySimpleGUI as sg
import pyautogui as pyg
import os
import sys
from Bot_Bc import StartingBot

x, y = pyg.position()

class Locposy:
    def __init__(self):
        #layout
        sg.theme('LightBrown4')
        line = [
            [sg.Text('Treasure Hunt:'), sg.Text('X:'), sg.Input(int(x), key='posXth', size=(8)),sg.Text('Y:'), sg.Input(int(y), key='posYth', size=(8)), sg.Button('Find_th')],
            [sg.Text('Button Heros: '), sg.Text('X:'), sg.Input(int(x), key='posXhr', size=(8)),sg.Text('Y:'), sg.Input(int(y), key='posYhr', size=(8)), sg.Button('Find_hr')],
            [sg.Text('Button Work:  '), sg.Text('X:'), sg.Input(int(x), key='posXwr', size=(8)),sg.Text('Y:'), sg.Input(int(y), key='posYwr', size=(8)), sg.Button('Find_wr')],
            [sg.Text('Button Reset: '), sg.Text('X:'), sg.Input(int(x), key='posXrs', size=(8)),sg.Text('Y:'), sg.Input(int(x), key='posYrs', size=(8)), sg.Button('Find_rs')],
            [sg.Text('Button Exit:    '), sg.Text('X:'), sg.Input(int(x), key='posXet', size=(8)),sg.Text('Y:'), sg.Input(int(y), key='posYet', size=(8)), sg.Button('Find_et')]

        ]

        layout = [
            [sg.Frame('Positions', layout=line, key='NewP')],
            [sg.Button('Start'), sg.Button('Save')]
        ]

        self.WinLocPosy = sg.Window('Boot', layout, finalize=True)

    def Start(self):
        while True:
            events, values = self.WinLocPosy.read()
            if events == sg.WIN_CLOSED:
                break

            elif events == 'Find_th':
                sg.popup('5 seconds for save a yours position curser')
                pyg.sleep(1)
                x, y = pyg.position()
                self.WinLocPosy['posXth'].update(int(x))
                self.WinLocPosy['posYth'].update(int(y))

            elif events == 'Find_hr':
                sg.popup('5 seconds for save a yours position curser')
                pyg.sleep(1)
                x, y = pyg.position()
                self.WinLocPosy['posXhr'].update(int(x))
                self.WinLocPosy['posYhr'].update(int(y))

            elif events == 'Find_wr':
                sg.popup('5 seconds for save a yours position curser')
                pyg.sleep(1)
                x, y = pyg.position()
                self.WinLocPosy['posXwr'].update(int(x))
                self.WinLocPosy['posYwr'].update(int(y))

            elif events == 'Find_rs':
                sg.popup('5 seconds for save a yours position curser')
                pyg.sleep(1)
                x, y = pyg.position()
                self.WinLocPosy['posXrs'].update(int(x))
                self.WinLocPosy['posYrs'].update(int(y))

            elif events == 'Find_et':
                sg.popup('5 seconds for save a yours position curser')
                pyg.sleep(1)
                x, y = pyg.position()
                self.WinLocPosy['posXet'].update(int(x))
                self.WinLocPosy['posYet'].update(int(y))

            elif events == 'Start':
                Locposy.StartBot(self)

            elif events == 'Save':
                Locposy.SaveLoc(self, values)

    def SaveLoc(self, values):
        with open('Config_bot.txt', 'w') as ark:
            ark.write("Treasure_Hunt:" + "\n" f"{values['posXth']}" + "\n" f"{values['posYth']}" + "\n"
            f"Button_Heros:" + "\n" f"{values['posXhr']}" + "\n" f"{values['posYhr']}" + "\n"
            f"Button_Work:" + "\n" f"{values['posXwr']}" + "\n" f"{values['posYwr']}" + "\n"
            f"Button_Reset:" + "\n" f"{values['posXrs']}" + "\n" f"{values['posYrs']}" + "\n"
            f"Button_Exit:" + "\n" f"{values['posXet']}" + "\n" f"{values['posYet']}" + "\n")

    def StartBot(self):
        if os.path.exists('Config_bot.txt'):
            print('arquivo existe')
            sg.popup_auto_close("please give us just the game's page, 5 sec for start the bot")
            pyg.sleep(5)
            StartingBot()

        else:
            sg.popup('Save not creat yet')

Locposy().Start()
