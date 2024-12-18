import pyautogui as py
from util.tempo import PauseApp

def PosicaoMouseTelaPC():
    print("------------------------")
    print("Posição do Mouse na Tela")
    print("------------------------")
    PauseApp(qtdeSeconds=5) 
    print(py.position())   
