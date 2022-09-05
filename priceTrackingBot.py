from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from TrendyolLoginInfo import username,password  
from email.message import EmailMessage
import ssl
import smtplib


import sys ## Ekrana hata mesajını bu modülle yazdırıcaz.



class Trendyol():
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        
        
    
    def signIn(self):
        self.browser.get("https://www.trendyol.com/giris?cb=https%3A%2F%2Fwww.trendyol.com%2F")
        self.browser.maximize_window()  
        time.sleep(2)
        
        eMail=self.browser.find_element_by_xpath("//*[@id='login-email']")
        eMail.send_keys(username)
        
        
        userPassword=self.browser.find_element_by_xpath("//*[@id='login-password-input']")
        userPassword.send_keys(password)
        
        signInButton=self.browser.find_element_by_xpath("//*[@id='login-register']/div[3]/div[1]/form/button")
        signInButton.click()
        
        time.sleep(2)
        
        

    def searchingLink(self,link):
        self.browser.get(link)
        
        self.priceOfLink=self.browser.find_element_by_xpath('.//span[@class = "prc-dsc"]')
        print(self.priceOfLink.text)
        self.priceOfLink=self.priceOfLink.text
        self.priceOfLink=self.priceOfLink.replace(",",".")
        self.priceOfLink=self.priceOfLink.replace("TL","")
        self.priceOfLink=self.priceOfLink.strip("")
        self.priceOfLink=int(self.priceOfLink)
        



    def mailSender(self):
        email_sender="myEmail@gmail.com"
        email_password="myPassword"
        email_receiver="emailReceiver@gmail.com"

        subject="Beklediğiniz İndirim!!"
        body="""
        Beklediğiniz ürünün istediğiniz indirimli fiyata ulaşmıştır..!
        BİLGİNİZE..
        """

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['subject']=subject
        em.set_content(body)
        
        
        context=ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                smtp.login(email_sender,"myEmailDataPasword")  ##BURAYA UYGULAMA ŞİFRESİNİN VERDİGİ ŞİFREYİ GİRİYORUZ.
                smtp.sendmail(email_sender, email_receiver,em.as_string())  
                print("Başarıyla gönderildi.")
        except:
            print("Bir hata meydana geldi...")
    
    
    
        
    
    
    def howMany(self,price):
        if self.priceOfLink<price:
            trendyol.mailSender()
            
            

        
        
        


trendyol=Trendyol(username,password)
trendyol.signIn()
trendyol.searchingLink("")
trendyol.howMany(400)