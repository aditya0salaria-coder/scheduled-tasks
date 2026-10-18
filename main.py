import os
import smtplib
import datetime as dt
import random

import pandas as pd

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


df = pd.read_csv("birthdays.csv")
print(df)

now = dt.datetime.now()
cu_year = now.year
cu_month = now.month
cu_day = now.day
letter_num = random.randint(1,3)

for index, row in df.iterrows():
    if(cu_month == row["month"] and cu_day == row["day"]):
        print(letter_num)
        with open(f"letter_templates/letter_{letter_num}.txt","r") as file:
            data = file.read()
            # print(data)
        data = data.replace("[NAME]",row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER,to_addrs=row["email"],msg=f"subject:HAPPY BIRTHDAY\n\n{data}")




