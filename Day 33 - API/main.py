import requests
import datetime as dt
import smtplib
import time

MY_LAT = 14.5995
MY_LONG = 120.9842    # Manila, Philippines

while True:
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.ConnectTimeout:
        print("Request to ISS API timed out. Retrying in 60 seconds...")
        time.sleep(60)
        continue

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # iss_latitude = 14
    # iss_longitude = 120    # For test purposes, set ISS position to Manila coordinates

    # If position is within +5 or -5 degrees of the ISS position.
    iss_near_loc = False
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        iss_near_loc = True

    print("My Coordinates:", MY_LAT, MY_LONG)
    print("ISS Coordinates:", iss_latitude, iss_longitude)
    print()

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Manila",  # Specify the timezone for sunrise/sunset times
    }

    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
        response.raise_for_status()
        data = response.json()
        sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    except requests.exceptions.ConnectTimeout:
        print("Request to Sunrise-Sunset API timed out. Retrying in 60 seconds...")
        time.sleep(60)
        continue

    time_now = dt.datetime.now()

    with open("../Day 32 - Send Emails and Manage Dates/email_details.txt", "r") as file:
        lines = [line.rstrip() for line in file]
        email_sender = lines[0]
        password = lines[1]

    if iss_near_loc and (time_now.hour <= sunrise_hour or time_now.hour >= sunset_hour):
        print("The ISS is close to your location and it is currently dark. Look up!")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email_sender, password=password)
            connection.sendmail(
            from_addr=email_sender, 
            to_addrs=email_sender, 
            msg=f"Subject:Look up, ISS nearby!\
            \n\nThe ISS is close to your location and it is currently dark. Beep boop..."
        )

    else: 
        print("Chile! the ISS is not close to your location or it is still light outside.")

    print()
    time.sleep(60)    # Run every 60 seconds
    print("------")
    print()
