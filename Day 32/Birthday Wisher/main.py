import smtplib
import random
from datetime import datetime 
import pandas

BIRTHDAY_PATH = 'Day 32\\Birthday Wisher\\birthdays.csv'
LETTERS_PATH = f'Day 32\\Birthday Wisher\\letter_templates\\letter_{random.randint(1,3)}.txt'


# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.






my_email = "testnutz420@gmail.com"
password = "dlaujqgdiwtbodda"

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mattsc298@gmail.com",
            msg=quote
            )


today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv(BIRTHDAY_PATH)

birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()} 

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(LETTERS_PATH) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        
        send_email(contents)

# if weekday == 4:

#     with open('Day 32\\Birthday Wisher\\quotes.txt', "r") as data:
#         quotes = data.readlines()

#     send_email(random.choice(quotes))