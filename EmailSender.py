# SMTP Kütüphanesi kullanarak Gmail üzerinden eposta gönderimi.
# Simple Mail Transfer Protocol

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Postala(isim,telefon,email,mesaj):
    eposta=MIMEMultipart()
    eposta["From"]=email
    eposta["To"]="test.altanemre1989@gmail.com"
    eposta["Subject"]=isim+"-"+telefon
    body=mesaj
    body_text=MIMEText(body,"plain")
    eposta.attach(body_text)
    try:
        gmail = smtplib.SMTP("smtp.gmail.com",587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login("test.altanemre1989@gmail.com","gbii holk rolr gtfe")
        gmail.sendmail(eposta["From"],eposta["To"],eposta.as_string())
        gmail.close()
    except:
        pass
