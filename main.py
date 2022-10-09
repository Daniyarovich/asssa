
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent


import pygsheets
import numpy as np
import requests
import sys 
import time
gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('ТЗ на таблицу')
wks1 = sh.worksheet_by_title("BYBIT-RUB")

def newmain():
    
    matrix = [] 
    a= []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a9 = []
    a10 = []
    a11 = []
    a12 = []
    def insertvalue(url, sdk, amount):
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        #options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        #options.add_argument("--headless")
        
        browser = webdriver.Chrome(executable_path="D:\\Bybit Parsing\\chromedriver\\chromedriver.exe", options = options)
        
        try:
            browser.get(url=url)
            amount_input=browser.find_elements(By.CLASS_NAME, "by-input__inner")
            
            amount_input[1].clear()
           
            amount_input[1].send_keys(amount)
            amount_input[1].send_keys(Keys.ENTER)
            try:
                l = browser.find_elements(By.CLASS_NAME, "price-amount")
                sdk.append(l[0].text)
            except Exception as ex:
                sdk.append("Пусто")   
            
          
            btc=browser.find_elements(By.CLASS_NAME, "by-switch__item")
            btc[3].click()
            
             
            amount_input=browser.find_elements(By.CLASS_NAME, "by-input__inner")
            amount_input[1].clear()
            amount_input[1].send_keys(amount)
            amount_input[1].send_keys(Keys.ENTER)
            try:
                l = browser.find_elements(By.CLASS_NAME, "price-amount")
                sdk.append(l[0].text)
            except Exception as ex:
                sdk.append("Пусто")   
            btc=browser.find_elements(By.CLASS_NAME, "by-switch__item")
            btc[4].click()
            
             
            amount_input=browser.find_elements(By.CLASS_NAME, "by-input__inner")
            amount_input[1].clear()
            amount_input[1].send_keys(amount)
            amount_input[1].send_keys(Keys.ENTER)
            try:
                l = browser.find_elements(By.CLASS_NAME, "price-amount")
                sdk.append(l[0].text)
            except Exception as ex:
                sdk.append("Пусто")   
            btc=browser.find_elements(By.CLASS_NAME, "by-switch__item")
            btc[5].click()
            
            time.sleep(1)
            amount_input=browser.find_elements(By.CLASS_NAME, "by-input__inner")
            amount_input[1].clear()
            amount_input[1].send_keys(amount)
            amount_input[1].send_keys(Keys.ENTER)
            try:
                l = browser.find_elements(By.CLASS_NAME, "price-amount")
                sdk.append(l[0].text)
            except Exception as ex:
                sdk.append("Пусто")   
            
            print(sdk)
           


        except Exception as ex:
            print(ex)
        finally:
            browser.close()
            browser.quit() 
    
    
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=75",a,"")
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=185",a1,"")  
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=377",a2,"")
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=274",a3,"")
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=64",a4,"") 
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=59",a5,"")  
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=44",a6,"")
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=102",a7,"")
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=379",a8,"") 
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=14",a9,"")  
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=51",a10,"")
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=5",a11,"")
    #insertvalue("https://www.binance.com/en/trade/BTC_BUSD?theme=dark&type=spot",a)        
    #insertvalue("https://www.binance.com/en/trade/BUSD_USDT?theme=dark&type=spot",a)        
    matrix.append(a) 
    matrix.append(a1)
    matrix.append(a2)
    matrix.append(a3) 
    matrix.append(a4) 
    matrix.append(a5)
    matrix.append(a6)
    matrix.append(a7)
    matrix.append(a8) 
    matrix.append(a9)
    matrix.append(a10)
    matrix.append(a11)
    wks1.update_values('B4-E15', matrix)    
   


    
    
while True:
    newmain()
    time.sleep(0)
    pass    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    