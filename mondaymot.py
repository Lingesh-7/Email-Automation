import datetime as dt
import random as r
import smtplib

monday=dt.datetime.now()
# print(monday.weekday())
my=os.environ.get("EMAIL_KEY")
password=os.environ.get("PASSWORD_KEY")
''''''
if monday.weekday()==0:
    with open(r"quotes.txt","r") as q:
        qoutes=q.read().split('\n')
    
    with smtplib.SMTP("smtp.gmail.com") as c:
        c.starttls()
        c.login(user=my,password=passwords)
        c.sendmail(from_addr=my,
        to_addrs="lingesh.91918@gmail.com",
        msg=f"Subject:Monday Motivation\n\n{r.choice(qoutes)}"
        )
        print("sent!!")

