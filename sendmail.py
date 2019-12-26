import os
import smtplib 
from email.message import EmailMessage

EMAIL_ADDRESS = 'example@gmail.com'  
EMAIL_PASSWORD = 'password'          
def send_mail(name,email_id):
    msg = EmailMessage()
    msg['Subject'] = 'Birtday wish' 
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email_id
    msg.set_content(f'Happy birtday {name.title()}')

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            try:
                smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp.send_message(msg)
                print("send succesfully\n")
            except TypeError:
                print("Couldn't send ! some error occured")

