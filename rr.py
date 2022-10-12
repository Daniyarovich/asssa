
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
    matrix1 = [] 
    matrix2=[]
    matrix3=[]
    matrix4=[]
    matrix5=[]
    matrix6=[]
    matrix7=[]
    
    a= []
    a1 = []
    a2 = []
    a3= []
    a4 = []
    a5 = []
    a6= []
    a7 = []
    
    
    b= []
    b1 = []
    b2 = []
    b3= []
    b4 = []
    b5 = []
    b6= []
    b7 = []
   

    c= []
    c1 = []
    c2 = []
    c3= []
    c4 = []
    c5 = []
    c6= []
    c7 = []

    d= []
    d1 = []
    d2 = []
    d3= []
    d4 = []
    d5 = []
    d6= []
    d7 = []
    
    
    e= []
    e1 = []
    e2 = []
    e3= []
    e4 = []
    e5 = []
    e6= []
    e7 = []

    f= []
    f1 = []
    f2 = []
    f3= []
    f4 = []
    f5 = []
    f6= []
    f7 = []
    def insertvalue(url, sdk,sdk1,sdk2,sdk3,sdk4,sdk5,sdk6,sdk7):
        
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        #options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        browser = webdriver.Chrome(executable_path=":\\Users\\Administrator\\Documents\\Binance\\ggmain\\Binance-SELL\\asssa\\chromedriver.exe", options = options)
        #options.add_argument("--headless")
        
            
        
        
        try:
            browser.get(url=url)
            amount_input1=browser.find_elements(By.CLASS_NAME, "by-dialog__close")
            amount_input1[0].click()
            def get_value(mat, amount):
                amount_input=browser.find_elements(By.CLASS_NAME, "by-input__inner")
                for i in range(len("2000000")):
                    amount_input[1].send_keys(Keys.BACKSPACE)
           
                amount_input[1].send_keys(amount)
                print("1")
                
                amount_input[1].send_keys(Keys.ENTER)
                time.sleep(1)
                print("1asd")
                try:
                    l = browser.find_elements(By.CLASS_NAME, "price-amount")
                    mat.append(l[0].text)
                except Exception as ex:
                    mat.append("Пусто")   
            

            
            
            
            
           
            get_value(sdk,"")
            
            get_value(sdk1,"1000")
            get_value(sdk2,"10000")
            get_value(sdk3,"20000")
            get_value(sdk4,"50000")
            get_value(sdk5,"80000")
            get_value(sdk6,"100000")
            get_value(sdk7,"200000")
            
            
             
                
           
            
            
            
           


        except Exception as ex:
            print(ex)
        finally:
            browser.close()
            browser.quit() 
    
    
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=BTC&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    matrix.append(a)
    matrix1.append(a1)
    matrix2.append(a2)
    matrix3.append(a3)
    matrix4.append(a4)
    matrix5.append(a5)
    matrix6.append(a6)
    matrix7.append(a7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=ETH&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDC&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    matrix.append(a)
    matrix1.append(a1)
    matrix2.append(a2)
    matrix3.append(a3)
    matrix4.append(a4)
    matrix5.append(a5)
    matrix6.append(a6)
    matrix7.append(a7)
   
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=BTC&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=ETH&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDC&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    matrix.append(b)
    matrix1.append(b1)
    matrix2.append(b2)
    matrix3.append(b3)
    matrix4.append(b4)
    matrix5.append(b5)
    matrix6.append(b6)
    matrix7.append(b7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=BTC&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=ETH&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
   
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDS&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
    matrix.append(c)
    matrix1.append(c1)
    matrix2.append(c2)
    matrix3.append(c3)
    matrix4.append(c4)
    matrix5.append(c5)
    matrix6.append(c6)
    matrix7.append(c7)
    wks1.update_values('B4-E6', matrix)    
    wks1.update_values('B18-E20', matrix1)   
    wks1.update_values('B32-E34', matrix2) 
    wks1.update_values('B46-E48', matrix3)    
    wks1.update_values('B60-E62', matrix4)   
    wks1.update_values('B74-E76', matrix5) 
    wks1.update_values('B88-E90', matrix6)    
    wks1.update_values('B102-E104', matrix7) 
     
    matrix.clear()
    matrix1.clear()
    matrix2.clear()
    matrix3.clear()
    matrix4.clear()
    matrix5.clear()
    matrix6.clear()
    matrix7.clear()
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDT&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    matrix.append(d)
    matrix1.append(d1)
    matrix2.append(d2)
    matrix3.append(d3)
    matrix4.append(d4)
    matrix5.append(d5)
    matrix6.append(d6)
    matrix7.append(d7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=BTC&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    matrix.append(d)
    matrix1.append(d1)
    matrix2.append(d2)
    matrix3.append(d3)
    matrix4.append(d4)
    matrix5.append(d5)
    matrix6.append(d6)
    matrix7.append(d7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=ETH&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    matrix.append(d)
    matrix1.append(d1)
    matrix2.append(d2)
    matrix3.append(d3)
    matrix4.append(d4)
    matrix5.append(d5)
    matrix6.append(d6)
    matrix7.append(d7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDC&fiat=RUB&paymentMethod=75",a, a1,a2,a3,a4,a5,a6,a7)
    matrix.append(d)
    matrix1.append(d1)
    matrix2.append(d2)
    matrix3.append(d3)
    matrix4.append(d4)
    matrix5.append(d5)
    matrix6.append(d6)
    matrix7.append(d7)
   
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDT&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    matrix.append(e)
    matrix1.append(e1)
    matrix2.append(e2)
    matrix3.append(e3)
    matrix4.append(e4)
    matrix5.append(e5)
    matrix6.append(e6)
    matrix7.append(e7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=BTC&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    matrix.append(e)
    matrix1.append(e1)
    matrix2.append(e2)
    matrix3.append(e3)
    matrix4.append(e4)
    matrix5.append(e5)
    matrix6.append(e6)
    matrix7.append(e7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=ETH&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    matrix.append(e)
    matrix1.append(e1)
    matrix2.append(e2)
    matrix3.append(e3)
    matrix4.append(e4)
    matrix5.append(e5)
    matrix6.append(e6)
    matrix7.append(e7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDC&fiat=RUB&paymentMethod=185",b, b1,b2,b3,b4,b5,b6,b7) 
    matrix.append(e)
    matrix1.append(e1)
    matrix2.append(e2)
    matrix3.append(e3)
    matrix4.append(e4)
    matrix5.append(e5)
    matrix6.append(e6)
    matrix7.append(e7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDT&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
    matrix.append(f)
    matrix1.append(f1)
    matrix2.append(f2)
    matrix3.append(f3)
    matrix4.append(f4)
    matrix5.append(f5)
    matrix6.append(f6)
    matrix7.append(f7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=BTC&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
    matrix.append(f)
    matrix1.append(f1)
    matrix2.append(f2)
    matrix3.append(f3)
    matrix4.append(f4)
    matrix5.append(f5)
    matrix6.append(f6)
    matrix7.append(f7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=ETH&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
    matrix.append(f)
    matrix1.append(f1)
    matrix2.append(f2)
    matrix3.append(f3)
    matrix4.append(f4)
    matrix5.append(f5)
    matrix6.append(f6)
    matrix7.append(f7)
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDS&fiat=RUB&paymentMethod=377",c, c1,c2,c3,c4,c5,c6,c7) 
    matrix.append(f)
    matrix1.append(f1)
    matrix2.append(f2)
    matrix3.append(f3)
    matrix4.append(f4)
    matrix5.append(f5)
    matrix6.append(f6)
    matrix7.append(f7)
      
    

    wks1.update_values('G4-J6', matrix)    
    wks1.update_values('G18-J20', matrix1)   
    wks1.update_values('G32-J34', matrix2) 
    wks1.update_values('G46-J48', matrix3)    
    wks1.update_values('G60-J62', matrix4)   
    wks1.update_values('G74-J76', matrix5) 
    wks1.update_values('G88-J90', matrix6)    
    wks1.update_values('G102-J104', matrix7)  
        
while True:
    newmain()
    time.sleep(0)
    pass    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
