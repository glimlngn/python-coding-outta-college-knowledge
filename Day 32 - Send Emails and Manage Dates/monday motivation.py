import smtplib
import datetime as dt
import random as r

with open("email_details.txt", "r") as file:
    lines = [line.rstrip() for line in file]

email_sender = lines[0]
password = lines[1]
email_recipient = lines[2]

now = dt.datetime.now()
if now.weekday() == 0:  # Monday is 0

    with open("quotes.txt", "r") as file:
        lines = [line.rstrip() for line in file]
        quote = r.choice(lines)

    print(quote)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(
            from_addr=email_sender, 
            to_addrs=email_recipient, 
            msg=f"Subject:Here's your Monday Motivation!\
            \n\n{quote}"
        )