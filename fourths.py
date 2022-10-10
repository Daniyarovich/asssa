
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
    def insertvalue(url, sdk,sdk1,sdk2,sdk3,sdk4,sdk5,sdk6,sdk7):
        
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        #options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        browser = webdriver.Chrome(executable_path="D:\\Bybit Parsing\\chromedriver\\chromedriver.exe", options = options)
        #options.add_argument("--headless")
        
            
        
        
        try:
            browser.get(url=url)
            def get_value(mat, amount):
                amount_input=browser.find_elements(By.CLASS_NAME, "by-input__inner")
                for i in range(len("2000000")):
                    amount_input[1].send_keys(Keys.BACKSPACE)
           
                amount_input[1].send_keys(amount)
                
                amount_input1=browser.find_elements(By.CLASS_NAME, "by-button--brand")
                amount_input1[0].click()
                time.sleep(1)
            
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
            
            btc=browser.find_elements(By.CLASS_NAME, "by-switch__item")
            btc[3].click()
            time.sleep(1)
            get_value(sdk,"")
            get_value(sdk1,"1000")
            get_value(sdk2,"10000")
            get_value(sdk3,"20000")
            get_value(sdk4,"50000")
            get_value(sdk5,"80000")
            get_value(sdk6,"100000")
            get_value(sdk7,"200000")
            
            btc=browser.find_elements(By.CLASS_NAME, "by-switch__item")
            btc[4].click()
            time.sleep(1)
            get_value(sdk,"")
            get_value(sdk1,"1000")
            get_value(sdk2,"10000")
            get_value(sdk3,"20000")
            get_value(sdk4,"50000")
            get_value(sdk5,"80000")
            get_value(sdk6,"100000")
            get_value(sdk7,"200000")
             
                
            btc=browser.find_elements(By.CLASS_NAME, "by-switch__item")
            btc[5].click()
            time.sleep(1)
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
    
    
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDT&fiat=RUB&paymentMethod=14",a, a1,a2,a3,a4,a5,a6,a7)
    matrix.append(a)
    matrix1.append(a1)
    matrix2.append(a2)
    matrix3.append(a3)
    matrix4.append(a4)
    matrix5.append(a5)
    matrix6.append(a6)
    matrix7.append(a7)
   
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDT&fiat=RUB&paymentMethod=51",b, b1,b2,b3,b4,b5,b6,b7) 
    matrix.append(a)
    matrix1.append(b1)
    matrix2.append(b2)
    matrix3.append(b3)
    matrix4.append(b4)
    matrix5.append(b5)
    matrix6.append(b6)
    matrix7.append(b7)
    
    insertvalue("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDT&fiat=RUB&paymentMethod=5",c, c1,c2,c3,c4,c5,c6,c7) 
    matrix.append(c)
    matrix1.append(c1)
    matrix2.append(c2)
    matrix3.append(c3)
    matrix4.append(c4)
    matrix5.append(c5)
    matrix6.append(c6)
    matrix7.append(c7)
   
    
    wks1.update_values('G13-J15', matrix)    
    wks1.update_values('G27-J30', matrix1)   
    wks1.update_values('G41-J43', matrix2) 
    wks1.update_values('G55-J57', matrix3)    
    wks1.update_values('G69-J71', matrix4)   
    wks1.update_values('G84-J86', matrix5) 
    wks1.update_values('G97-J99', matrix6)    
    wks1.update_values('G111-J113', matrix7)   
    

    
    
while True:
    newmain()
    time.sleep(0)
    pass    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    