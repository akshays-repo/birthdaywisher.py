import os
import smtplib 
from email.message import EmailMessage

EMAIL_ADDRESS = 'example@gmail.com'   #sender email id goes here -> replace the email id 
EMAIL_PASSWORD = 'password'           # password of user -> replace the password
def send_mail(name,email_id):
    msg = EmailMessage()
    msg['Subject'] = 'Happy Birthday '+name.title() #email subject
    msg['From'] = EMAIL_ADDRESS     #sender email id 
    msg['To'] = email_id            #reciever email id 
    msg.set_content('Happy Birthday'+name.title()+'')# content of email

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            try:
                smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp.send_message(msg)
                print("send succesfully\n")
            except TypeError:
                print("Couldn't send ! some error happend")

