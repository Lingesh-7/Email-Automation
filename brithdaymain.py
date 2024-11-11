import pandas as p
import datetime as dt
import random as r
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
brithday=p.read_csv(r"C:\Users\linge\Desktop\python 100 days\projects\pr-32\letter_templates\birthdays.csv")
# print(brithday.to_dict(orient="records"))
brithdata=brithday.to_dict(orient="records")
# print(brithdata)
my=os.environ.get("EMAIL_KEY")
password=os.environ.get("PASSWORD_KEY")
to=dt.datetime.now()
today=to.day
tomonth=to.month
for i in brithdata:
    if today==int(i['day']) and tomonth==int(i['month']):
        l=[r"C:\Users\linge\Desktop\python 100 days\projects\pr-32\letter_templates\letter_1.txt",r"C:\Users\linge\Desktop\python 100 days\projects\pr-32\letter_templates\letter_2.txt",r"C:\Users\linge\Desktop\python 100 days\projects\pr-32\letter_templates\letter_3.txt"]
        randl=r.choice(l)
        with open(f"{randl}","r") as re:
            c=re.read()
        newc=c.replace('NAME,',f"{i['name']}")
        with smtplib.SMTP("smtp.gmail.com") as c:
            c.starttls()
            c.login(user=my,password=password)
            c.sendmail(from_addr=my,to_addrs=f"{i['email']}",msg=f"Subject:HAPPY BRITHDAY\n\n{newc}")

    # else:
    #     print("None")


