import pandas
import json
import sendmail
from datetime import datetime

#convert excel data to json then to Dict 
excel_data = pandas.read_excel('dob.xlsx')
json_data = excel_data.to_json(orient='records')
data = json.loads(json_data)

def checkbirtday(data,choice):
    for person in data: 
        try:
            dateofbirth_srt = str(person['DOB'])
            dateofbirth_object=datetime.strptime(dateofbirth_srt,'%d:%m:%y')
            day = dateofbirth_object.day
            month = dateofbirth_object.month
            email_id =person['EMAIL']
            name = person['NAME']
        except TypeError:
                pass
        if choice == '1':
            if person['DOB'] != None:
                print('*' * 20)
                print(f'Name :{name}')
                print(f'Email :{email_id}')
                print(f'Date of Birth :{dateofbirth_object}')
            else:
                pass
        elif choice == '2' and dateofbirth_srt != None:
            #get current day and month
            d =datetime.today()
            currentmonth = d.month
            currentday = d.day
            
            #check today is bday or not 
            if str(day) == str(currentday) and str(month) == str(currentmonth):
                print(f'Today is {name.title()} birtday.')
                print(f'Sending a Wish to {name}.' )
                sendmail.send_mail(name,email_id)  #send mail 
            else:
                 print(f'Today is not {name} birthday')
        else:
            pass


#Begin 
print('\n\nWelcome to PYTHON BIRTH BOT')
print(' ****************************')
choice = '1'
while choice != '3':
    choice = input("\nEnter your choice \n 1.View the users\n 2.Send the wishes\n 3.Exit\n >>  ")
    checkbirtday(data,choice)


        
