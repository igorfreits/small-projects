import pyperclip
import pyautogui
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

pyautogui.PAUSE = 1
pyautogui.hotkey('win', 'm')
pyautogui.press('1')
pyautogui.press('Enter')
time.sleep(1)
pyautogui.press('down')
pyautogui.press('f2')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'f4')

navegador = webdriver.Chrome()
navegador.get(
    'https://tecnolatina365.sharepoint.com/sites/PedidosdeVenda5/Lists/Pedidos%20de%20Venda/Agrupado%20Status.aspx')

time.sleep(1)
navegador.find_element(
    By.XPATH, '//*[@id="i0116"]').send_keys('qualidade@tecnolatina.com.br')
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('Tcl@2021')
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
navegador.find_element(
    By.XPATH, '//*[@id="sbcId"]/form/input').send_keys(Keys.CONTROL + 'v')
time.sleep(1)
navegador.find_element(
    By.XPATH, '//*[@id="sbcId"]/form/input').send_keys(Keys.BACKSPACE)
navegador.find_element(
    By.XPATH, '//*[@id="sbcId"]/form/input').send_keys(Keys.BACKSPACE)
navegador.find_element(
    By.XPATH, '//*[@id="sbcId"]/form/input').send_keys(Keys.BACKSPACE)
navegador.find_element(
    By.XPATH, '//*[@id="sbcId"]/form/input').send_keys(Keys.CONTROL + 'a')
navegador.find_element(
    By.XPATH, '//*[@id="sbcId"]/form/input').send_keys(Keys.CONTROL + 'c')
navegador.find_element(
    By.XPATH, '//*[@id="sbcId"]/form/input').send_keys(Keys.ENTER)

time.sleep(5)
pyautogui.doubleClick(x=735, y=484)
time.sleep(2)
navegador.find_element(By.XPATH,
                       '//*[@id="appRoot"]/div[2]/div/div[4]/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/div[3]/div/div[8]/div[2]/div'
                       ).click()
time.sleep(2)
pyautogui.write('SIM')
time.sleep(2)
pyautogui.press('Enter')

time.sleep(3)
pyautogui.press('Tab')
time.sleep(2)
pyautogui.press('Tab')
time.sleep(2)
pyautogui.press('Tab')
time.sleep(2)
pyautogui.press('Tab')
time.sleep(2)
pyautogui.press('Enter')

time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id="appRoot"]/div[2]/div/div[4]/div[2]/div/div[4]/div/div/div[2]/div/div/div/div/div[4]/div/div/span/div[1]/div/div[2]/button'
                       ).click()
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('1')
pyautogui.press('Enter')


time.sleep(2)
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('Enter')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
time.sleep(2)
pyautogui.press('Enter')

time.sleep(5)

navegador.quit()

time.sleep(2)
pyautogui.hotkey('win', 'm')
time.sleep(2)
pyautogui.press('1')
pyautogui.press('Enter')
time.sleep(2)
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'x')
time.sleep(2)
pyautogui.hotkey('win', 'm')
time.sleep(2)
pyautogui.press('2')
time.sleep(2)
pyautogui.press('Enter')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.hotkey('alt', 'f4')

exec(open('Automação de Processos - envio de laudos.py').read())
