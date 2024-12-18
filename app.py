#https://www.youtube.com/watch?v=11BQDtAjW5w&t=124s
import pyautogui as pa
import webbrowser as wb
from moduleMouse.clicks import (ClickDinamic)
from util.tempo import PauseApp                                
from util.gettingMouseScreen import PosicaoMouseTelaPC



# abrindo a pagina do google
wb.open("https://www.google.com.br")
ClickDinamic(strLocaleClick="Click Conta Google",valueX=1334,valueY=134)
ClickDinamic(strLocaleClick="Button Mostrar Mais Contas",valueX=1295,valueY=449)
ClickDinamic(strLocaleClick="Click Conta ICPV",valueX=1122,valueY=583)
ClickDinamic(strLocaleClick="Click gmail",valueX=1167,valueY=138)

PosicaoMouseTelaPC()