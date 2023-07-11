import datetime as dt
import random
import smtplib
import pandas

PLACEHOLDER = "[NAME]"
my_email = "adamosayinghi@gmail.com"
password = "tqlfrjigxyetsixn"

now = dt.datetime.now()
month = now.month
day = now.day

date_of_birth = dt.datetime(year=1999, month=7, day=9)

data = pandas.read_csv("birthdays.csv")
names = data["name"].to_list()
random_number = random.randint(1, 3)

with open(f"./letter_templates/letter_{random_number}.txt", mode="r") as letter_file:
    letter = letter_file.read()
    for name in names:
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"./ready_to_send_letter/birthday_wisher_{name}.txt", mode="w") as completed_birthday_wisher:
            completed_birthday_wisher.write(new_letter)
        with open(f"./ready_to_send_letter/birthday_wisher_{name}.txt", mode="r") as completed_birthday_wisher:
            birthday = completed_birthday_wisher.read()
        if (date_of_birth.month == month) and (date_of_birth.day == day):
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="adamosayinghi@yahoo.com",
                                    msg=f"Subject:Happy Birthday!\n\n{birthday}")


