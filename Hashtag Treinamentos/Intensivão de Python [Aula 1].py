import pandas as pd
import pyautogui
import pyperclip
import time
import numpy

pyautogui.PAUSE = 1

pyautogui.hotkey('win')
pyautogui.write('opera')
pyautoguiS.press('enter')
pyperclip.copy(
    'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')

pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)
pyautogui.PAUSE = 2
pyautogui.position(x=387, y=294)
pyautogui.doubleClick(x=387, y=294)
pyautogui.click(x=387, y=294)
pyautogui.click(x=1238, y=190)
pyautogui.click(x=1156, y=596)


tabela = pd.read_excel(
    r'C:\Users\Igor\Desktop\Estudos\Programação em Python\Hashtag Treinamentos\Base de dados hastag\Vendas - Dez.xlsx')
print(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

pyautogui.hotkey('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=79, y=201)
time.sleep(3)
pyautogui.write('pythonimpressionador+diretoria@gmail.com')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write('Relatório de Vendas')
pyautogui.press('Tab')
time.sleep(3)

texto = f"""
Prezados, bom dia
O faturamento de ontem foi de R$: {faturamento:,.2f}
e tivemos um total de: {quantidade:,} vendas.
Abraços, Igor F 
"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')


print(pyautogui.position())
