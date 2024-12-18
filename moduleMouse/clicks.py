import pyautogui as py
from util.tempo import PauseApp

'''
Pc Tonis Torres

* Posição Click Google Apps : valueX=1275,valueY=144
* Posição Click Conta Google: valueX=1334,valueY=134

'''



def ClickDinamic(valueX, valueY, strLocaleClick):
    print("---------------------") 
    print(f"Click {strLocaleClick}")
    print("---------------------")
    PauseApp(qtdeSeconds=5)
    py.click(x=valueX, y=valueY)
    
    