import time
from selenium.webdriver.common.keys import Keys
from selenium import  webdriver
import os
from selenium.webdriver.common.by import By
os.environ['path'] += r"C:/selenium drivers"
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
print("scan QR press enter")
input()

def logout():
 user=input("do you want to log out")
 
 if (user == "yes"):
  menu_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[4]/div/span')
  menu_button.click()
  time.sleep(3)
  logout_name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div/ul/li[5]/div')
  logout_name.click()
  time.sleep(2)
  logout_name=driver.find_element(By.XPATH,'/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div')
  logout_name.click()
  time.sleep(2)

 elif(user == "no"):
  msg()
 else:
    print("invalide")
    anyone()
def msg():
   receiver = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
   print("enter the name of contract:")
   name=input()
   receiver.send_keys(name,Keys.ENTER)
   receiver.click()
   time.sleep(2)
   mesage_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p') 
   print("enter the message :")
   message=input()
   mesage_box.send_keys(message, Keys.ENTER)
   time.sleep(5)
msg()
def anyone():
    choice="yes"
    while(choice !="no"):
     ask=input("do you want tosend message to anyone else :")
     if(ask == "yes"):
        msg()
        anyone()
        time.sleep(2)
     elif(ask =="no"):
        time.sleep(2)
        logout()
     else:
        print("invalid do it again")
        time.sleep(2)
        msg()
    choice="no"
anyone()
 




   
 


