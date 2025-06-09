import smtplib
import datetime as dt
import random as r
import pandas as pd
import glob    # To check files in a directory (weird name)

now = dt.datetime.now()

with open("email_details.txt", "r") as file:
    lines = [line.rstrip() for line in file]
    email_sender = lines[0]
    password = lines[1]

with open("birthdays.csv", "r") as file:
    birthdays = pd.read_csv(file)
    birthdays = pd.DataFrame(birthdays)    # Dynamic typing FTW

letter_templates = [file.removeprefix("letter_templates\\") for file in glob.glob("letter_templates/*.txt")]
with open(f"letter_templates/{r.choice(letter_templates)}", "r") as file:
    template = file.read()    # Select a random letter template

for index, row in birthdays.iterrows():
    if row["month"] == now.month and row["day"] == now.day:
        letter = template.replace("[NAME]", row["name"])    # Replace placeholder with actual name
        print(letter)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email_sender, password=password)
            connection.sendmail(
            from_addr=email_sender, 
            to_addrs=row["email"], 
            msg=f"Subject:Happy Birthday!\
            \n\n{ letter}"
        )