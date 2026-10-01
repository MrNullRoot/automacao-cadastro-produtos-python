import os
import time
import webbrowser
import pandas
import pyautogui

pyautogui.PAUSE = 1.0

webbrowser.open("http://127.0.0.1:5500/index.html")
time.sleep(2)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
  
    codigo = str(tabela.loc[linha, "Codigo_Produto"])
    nome = str(tabela.loc[linha, "Nome_Produto"])
    categoria = str(tabela.loc[linha, "Categoria"])
    preco = str(tabela.loc[linha, "Preco"])

   
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(nome)
    pyautogui.press("tab")

    pyautogui.write(categoria)
    pyautogui.press("tab")

    pyautogui.write(preco)
    pyautogui.press("tab")

    pyautogui.press("enter")
   
