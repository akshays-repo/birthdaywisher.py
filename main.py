import pandas
import json
import datetime
import sendmail

#convert excel data to json then to Dict 
excel_data = pandas.read_excel('dob.xlsx')
json_data = excel_data.to_json(orient='records')
data = json.loads(json_data)

def checkbirtday(data,choice):
    for person in data:
        # Assign user info to variables 
        try:
            date_of_birth = person['DOB']
            day = date_of_birth[0:2]
            month = date_of_birth[3:5]
            year = date_of_birth[6:10]
            email_id =person['EMAIL']
            name = person['NAME']
        except TypeError:
                pass
        if choice == '1':
            if person['DOB'] != None:
                print('*' * 20)
                print("Name :" ,name)
                print("Email :",email_id)
                print('Date of Birth :',date_of_birth)
            else:
                pass
        elif choice == '2' and date_of_birth != None:
            #get current day and month
            d =datetime.datetime.today()
            currentmonth = d.month
            currentday = d.day
            
            #check today is bday or not 
            if str(day) == str(currentday) and str(month) == str(currentmonth):
                print("Today is ",name.title()+' birtday.')
                print("Sending a Wish to ",name +"." )
                sendmail.send_mail(name,email_id)  #send mail 
            else:
                print("Today is not ",name +' birtday.')
        else:
            pass


#Begin 

print('\n\nWelcome to BIRTHDAY_EMAIL BOT')
print(' ****************************')
choice = '1'
while choice != '3':
    choice = input("\nEnter your choice \n 1.View the users\n 2.Send the wishes\n 3.Exit\n >>  ")
    checkbirtday(data,choice)


        